from pathlib import Path
import re
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import json

from app.adapter.gemini import connect_gemini
from app.adapter.postgresql import connect_postgresql
from app.adapter.gemini import prompt_insert
from app.features.mock_data import extract_table_name_from_sql_command, generate_mock_data

sql_files = [
    "./operational_query/create_masterdata.sql",
    "./operational_query/create_transactional_data.sql",
    "./operational_query/create_timeseries_data.sql"
]

table_schema = """c
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
    # gemini_client = connect_gemini()


    # mock_data = generate_mock_data(gemini_client=gemini_client,
    #                    table_schema=table_schema,
    #                    n=1)

    # print(mock_data)



    # extract_table_name_from_sql_command(gemini_client=gemini_client,
    #                                     )

    tables = extract_table_names_from_files(file_paths=sql_files)


    existing_tables, missing_tables = check_tables_exist(cursor=postgresql_cursor, table_list=tables, schema="happymeal")

    # print("existing_tables : ", existing_tables, " missing_tables : ",missing_tables)

    print(f"missing tables : {missing_tables}")
    if missing_tables:
        # print("sql_files : ", sql_files)
        for table in missing_tables:
            script = None
            for sql_file in sql_files:
                content = Path(sql_file).read_text()
                # print("content : ", content)
                stmt = extract_create_table(sql_text=content, table_name=table)
                # print(f"table = {table}, stmt = {stmt}, sql_file = {sql_file}")
                # print("sql_file = ", sql_file)
                if stmt:
                    script = stmt
                    print(script)
                    break
            print("table : ", table, " stmt = ", stmt)
            if script is not None:
                create_table(cursor=postgresql_cursor, sql_script=script)




    # content = Path("./operational_query/create_masterdata.sql").read_text()
    # # print("content : ", content)
    # stmt = extract_create_table(sql_text=content, table_name="meal_plan_types")
    # print(stmt)

def create_table(cursor, sql_script: str):
    cursor.execute(sql_script,)


def check_tables_exist(cursor, table_list, schema):
    query = """
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = %s
        AND table_name = ANY(%s)
    """

    cursor.execute(query, (schema, table_list))
    
    existing_tables = [row[0] for row in cursor.fetchall()]

    # Find missing tables
    missing_tables = list(set(table_list) - set(existing_tables))

    return existing_tables, missing_tables

    


def extract_table_names_from_files(file_paths):
    table_names = []

    # Regex to match table names in CREATE TABLE statements
    pattern = re.compile(r"CREATE TABLE\s+([^\s(]+)", re.IGNORECASE)

    for file_path in file_paths:
        content = Path(file_path).read_text()  # Read file content
        matches = pattern.findall(content)
        table_names.extend(matches)
    
    return table_names

def extract_create_table(sql_text: str, table_name: str) -> str:
    """
    Extracts the CREATE TABLE statement for a specific table from a SQL script.
    
    Args:
        sql_text (str): The full SQL script as a string.
        table_name (str): The table name to extract.
    
    Returns:
        str: The CREATE TABLE statement, or empty string if not found.
    """
    # Regex pattern to capture CREATE TABLE statements
    pattern = rf"(CREATE TABLE\s+{table_name}\s*\(.*?\);)"
    
    # re.DOTALL allows . to match newlines
    match = re.search(pattern, sql_text, re.IGNORECASE | re.DOTALL)
    
    if match:
        return match.group(1)
    else:
        return ""



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