import sqlite3
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "analytics.db")

def load_table(table_name: str) -> pd.DataFrame:
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df

if __name__ == "__main__":
    print(load_table('user_mart'))