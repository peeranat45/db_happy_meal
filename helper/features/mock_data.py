

import json
from app.adapter.gemini import prompt_insert


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


def extract_table_name_from_sql_command(gemini_client, sql_content: str) -> list:
     prompt = f"""
        You are a SQL parser. Given the following SQL content, extract all table names defined in CREATE TABLE statements.

        SQL Content:
        {sql_content}

        Return output only as a Python list of table names. Do not include any explanations.
    """

