import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

from app.adapter.gemini import connect_gemini

def connect_postgresql():
    load_dotenv()
    password = os.getenv("PASSWORD")
    host = os.getenv("HOST")
    port = os.getenv("PORT")
    user = os.getenv("DB_USER")
    print("user : ", user)

    # Define your connection string
    conn_str = f"postgresql://{user}:{password}@{host}:{port}/postgres"

    print(conn_str)

    conn = None
    cursor = None
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(conn_str)
        cursor = conn.cursor()

        # Example query
        cursor.execute("SHOW search_path;")
        record = cursor.fetchone()
        print("Connected successfully!")
        print("PostgreSQL version:", record)

        # Set the default schema for this session
        cursor.execute('SET search_path TO happymeal, public;')

        # Verify it worked
        cursor.execute('SHOW search_path;')
        print("Search path:", cursor.fetchone())

        # Example query (no need to prefix schema now)
        cursor.execute("SELECT * FROM users;")
        record = cursor.fetchone()
        print(record)
        connect_gemini()

    except Exception as e:
        print("Error connecting to PostgreSQL:", e)

    return cursor, conn
    