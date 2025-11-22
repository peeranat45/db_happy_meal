import json
import os
import time
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

# ========== CONFIG ==========
load_dotenv()  # Load environment variables from .env file

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1")
BATCH_FILE = os.getenv("BATCH_FILE", "./data/batch_requests.jsonl")
OUTPUT_FILE = os.getenv("OUTPUT_FILE", "./data/batch_output.jsonl")
# ============================

client = OpenAI(api_key=OPENAI_API_KEY)

# ---------- Fetch schema & sample data ----------
def fetch_schema_and_existing_data():
    conn = psycopg2.connect(
        host=DB_HOST, port=DB_PORT, database=DB_NAME,
        user=DB_USER, password=DB_PASS
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema='public'
          AND table_name NOT LIKE 'alembic_version'
    """)
    tables = [t["table_name"] for t in cur.fetchall()]

    schema = {}
    existing_data = {}

    for table in tables:
        cur.execute(f"""
            SELECT column_name, data_type
            FROM information_schema.columns
            WHERE table_name='{table}' AND table_schema='public'
        """)
        schema[table] = cur.fetchall()

        cur.execute(f"SELECT * FROM {table} LIMIT 20")
        existing_data[table] = cur.fetchall()

    cur.close()
    conn.close()
    return schema, existing_data

# ---------- Build prompt ----------
def build_prompt(scenario, schema, existing_data):
    return f"""
You are a database mock data generator AI.
Generate realistic data for the given scenario.

Goal: Generate new realistic data across ALL related tables. 
Condition: Only Thai People, Data range within 1 Jan 2024 until now, Since users created. You must generate transactional data of that users everyday since user created 
for example if user created data since 1 Oct 2025, You must create meals since 1 Oct 2025 - Now every day. Applied to other transaction data table also
If there are already data on master data table you can reuse existing data or create new one

### DATABASE SCHEMA ###
{json.dumps(schema, indent=2, default=str)}

### EXISTING SAMPLE DATA ###
{json.dumps(existing_data, indent=2, default=str)}

### USER SCENARIO ###
{scenario}

### OUTPUT FORMAT (STRICT JSON ARRAY) ###
[
  {{
    "table": "<table_name>",
    "rows": [
      {{ ... }},
      {{ ... }}
    ]
  }},
  ...
]

IMPORTANT: Only include the columns that exist in the schema.  
Do not add extra fields. Do not include explanations or comments. Output must be valid JSON.
"""

# ---------- Create batch request ----------
def create_batch_request_file(prompt):
    with open(BATCH_FILE, "w", encoding="utf-8") as f:
        request_obj = {
            "custom_id": "generate_mock_data",
            "method": "POST",
            "url": "/v1/responses",
            "body": {
                "model": MODEL_NAME,
                "input": prompt,
                "temperature": 0.4
            }
        }
        f.write(json.dumps(request_obj) + "\n")

# ---------- Submit batch ----------
def submit_batch():
    input_file = client.files.create(
        file=open(BATCH_FILE, "rb"),
        purpose="batch"
    )
    batch = client.batches.create(
        input_file_id=input_file.id,
        endpoint="/v1/responses",
        completion_window="24h"
    )
    print("Batch ID:", batch.id)
    return batch.id

# ---------- Wait for batch ----------
def wait_for_batch(batch_id):
    print("Waiting for batch to complete...")
    while True:
        batch = client.batches.retrieve(batch_id)
        print("Status:", batch.status)
        if batch.status == "completed":
            return batch.output_file_id
        if batch.status == "failed":
            raise Exception("Batch failed!")
        time.sleep(5)

# ---------- Download batch output ----------
def download_output(output_file_id):
    result = client.files.content(output_file_id)
    with open(OUTPUT_FILE, "wb") as f:
        f.write(result.read())
    print("Output saved to:", OUTPUT_FILE)

# ---------- Parse batch result ----------
def parse_batch_result():
    tables_data = []
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            body = obj.get("response", {}).get("body", {})
            outputs = body.get("output", [])
            if not outputs:
                continue
            content_blocks = outputs[0].get("content", [])
            full_text = "".join(
                block["text"]
                for block in content_blocks
                if block.get("type") == "output_text"
            )
            try:
                parsed_json = json.loads(full_text)
                if isinstance(parsed_json, list):
                    tables_data.extend(parsed_json)
                else:
                    tables_data.append(parsed_json)
            except Exception as e:
                print("Failed to parse JSON:", e)
    return tables_data

TABLE_ORDER = [
  "users",
  "diseases",
  "eating_lifestyle_categories",
  "social_platforms",
  "meal_types",
  "locations",
  "ingredients",
  "exercise_types",
  "meal_plan_types",
  "channels",
  "medical_histories",
  "eating_lifestyles",
  "user_allergics",
  "user_social_accounts",
  "user_statistics",
  "foods",
  "food_ingredients",
  "meals",
  "food_meals",
  "favorite_foods",
  "exercises",
  "meal_plans",
  "meal_plan_foods",
  "favorite_meal_plans",
  "drinkings"
]


# ---------- Insert generated data ----------
def insert_generated_data(tables_data):
    conn = psycopg2.connect(
        host=DB_HOST, port=DB_PORT, database=DB_NAME,
        user=DB_USER, password=DB_PASS
    )
    cur = conn.cursor()

    # Create a dict for faster lookup
    data_dict = {t["table"]: t["rows"] for t in tables_data}

    # Insert in dependency order
    for table_name in TABLE_ORDER:
        rows = data_dict.get(table_name, [])
        if not rows:
            continue

        columns = rows[0].keys()
        col_names = ", ".join(columns)
        placeholders = ", ".join(["%s"] * len(columns))
        insert_query = f"INSERT INTO {table_name} ({col_names}) VALUES ({placeholders})"

        for row in rows:
            values = []
            for col in columns:
                v = row[col]
                if isinstance(v, str):
                    values.append(v)
                elif isinstance(v, (int, float)):
                    values.append(v)
                elif v is None:
                    values.append(None)
                else:
                    try:
                        values.append(datetime.fromisoformat(str(v)))
                    except:
                        values.append(str(v))
            cur.execute(insert_query, values)

    conn.commit()
    cur.close()
    conn.close()
    print("Inserted generated data into the database in dependency order.")

# ---------- MAIN ----------
def main():
    print("Reading DB schema + data...")
    schema, existing_data = fetch_schema_and_existing_data()

    print("\nEnter your scenario:")
    scenario = input("> ")

    prompt = build_prompt(scenario, schema, existing_data)
    create_batch_request_file(prompt)

    batch_id = submit_batch()
    output_file_id = wait_for_batch(batch_id)
    download_output(output_file_id)

    tables_data = parse_batch_result()
    print("\n=== GENERATED TABLE DATA ===")
    print(json.dumps(tables_data, indent=2, default=str))

    insert_generated_data(tables_data)

if __name__ == "__main__":
    main()
