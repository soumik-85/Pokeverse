import os
import psycopg2
from dotenv import load_dotenv

load_dotenv("config.env")

DATABASE_URL = os.getenv("DATABASE_URL")

try:
    connection = psycopg2.connect(DATABASE_URL)

    print("PostgreSQL connection successful!")

    connection.close()

except Exception as e:
    print("Connection failed:", e)