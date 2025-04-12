import streamlit as st
import time 
import psycopg2
from psycopg2 import OperationalError
import logging

# Configure logging 
logging.basicConfig(level=logging.INFO)

# Define the connection parameters
DB_HOST = "postgres"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "postgres"
DB_PORT = 5432

def fetch_data():
  try:
    conn = psycopg2.connect(
      host=DB_HOST,
      database=DB_NAME,
      user=DB_USER,
      password=DB_PASS,
      port=DB_PORT
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sentences")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
  except OperationalError as e:
    st.err(f"OperationalError : {e}")
    return []
  except Exception as e:
    return []

def main():
  st.title('Sentence Data dashboard')
  st.write("Here is your sentiment analysis on sentence data:")

  unique_id = set()

  while True:
    data = fetch_data()
    if data:
      for row in data:
        id = row[0]
        if id in unique_id:
          continue 
        st.write(row)
        unique_id.add(id)
    else:
      st.write("")
    time.sleep(5)


if __name__ == "__main__":
  main()