import os
import pandas as pd
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DATA_DIR = "./data/pos_files"  # Adjust directory path

# Setup logging
logging.basicConfig(
    filename="etl_process.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def connect_to_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        logging.info("Database connection established.")
        return conn
    except Exception as e:
        logging.error(f"Failed to connect to the database: {e}")
        raise

def process_files(conn):
    files = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")]
    for file in files:
        try:
            file_path = os.path.join(DATA_DIR, file)
            df = pd.read_csv(file_path)
            table_name = os.path.splitext(file)[0]

            # Create table dynamically
            create_table(conn, df, table_name)

            # Load data
            load_data(conn, df, table_name)
            logging.info(f"Successfully processed file: {file}")
        except Exception as e:
            logging.error(f"Failed to process file {file}: {e}")

def create_table(conn, df, table_name):
    try:
        columns = ", ".join([f"{col} TEXT" for col in df.columns])  # Adjust types as needed
        create_query = sql.SQL(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});")
        with conn.cursor() as cursor:
            cursor.execute(create_query)
            conn.commit()
        logging.info(f"Table {table_name} created/exists.")
    except Exception as e:
        logging.error(f"Failed to create table {table_name}: {e}")
        raise

def load_data(conn, df, table_name):
    try:
        with conn.cursor() as cursor:
            for _, row in df.iterrows():
                values = tuple(row.values)
                insert_query = sql.SQL(
                    f"INSERT INTO {table_name} VALUES ({', '.join(['%s'] * len(values))});"
                )
                cursor.execute(insert_query, values)
            conn.commit()
        logging.info(f"Data loaded into table {table_name}.")
    except Exception as e:
        logging.error(f"Failed to load data into table {table_name}: {e}")
        raise

if __name__ == "__main__":
    conn = connect_to_db()
    process_files(conn)
    conn.close()
    logging.info("ETL process completed.")
