import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import json

from app.adapter.gemini import connect_gemini
from app.adapter.postgresql import connect_postgresql
from app.adapter.gemini import prompt_insert

table_schema = """
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	dob TIMESTAMP WITH TIME ZONE NOT NULL,
	gender TEXT NOT NULL,
	target_weight REAL NOT NULL,
	drinking_goal REAL NOT NULL,
	is_vegan boolean NULL,
	nationality TEXT NULL,
	occupation TEXT NULL,
	income_value REAL NULL,
	company_name TEXT NULL,
	user_activity_level TEXT NOT NULL,
	exercise_frequency REAL NOT NULL,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
	last_active TIMESTAMP WITH TIME ZONE NOT NULL
);
"""

def main():
    postgresql_cursor, conn = connect_postgresql()
    gemini_client = connect_gemini()


    mock_data = generate_mock_data(gemini_client=gemini_client,
                       table_schema=table_schema,
                       n=1)

    print(mock_data)
def generate_mock_data(gemini_client, table_schema: str, n : int) -> dict:

    prompt = f"""
    You are a data generator. Given this SQL table schema, generate {n} rows of mock data as JSON array.
    
    Table Schema:
    {table_schema}
    
    Return output only as JSON array of objects. Do not include any explanations.
    """
    response = prompt_insert(gemini_client, prompt)

    # Remove any unwanted words (like 'json') if needed
    response = response.replace("json", "")
    response = response.replace("```", "")

    print("response : ", response)

    # Parse the string as JSON
    mock_data = json.loads(response)
    
    return mock_data




def force_drop_table(cursor,conn):
    cursor.execute("SET session_replication_role = 'replica';")

    # Generate DROP TABLE statements for all tables in 'public' schema
    cursor.execute("""
        SELECT tablename
        FROM pg_tables
        WHERE schemaname = 'public';
    """)
    tables = cursor.fetchall()

    for table in tables:
        cursor.execute(f'DROP TABLE IF EXISTS "{table[0]}" CASCADE;')
        print(f'Dropped table {table[0]}')

    # Re-enable constraints
    cursor.execute("SET session_replication_role = 'origin';")
    conn.commit()
    print("All tables dropped successfully!")

if __name__ == "__main__":
    main()