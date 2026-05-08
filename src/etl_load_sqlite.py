import pandas as pd
import sqlite3
import os

def load_csv_to_sqlite():
    csv_path = 'data/raw/customers_raw.csv'
    db_path = 'data/db/analytics.db'
    
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    df = pd.read_csv(csv_path)
    
    conn = sqlite3.connect(db_path)
    
    df.to_sql('customers_raw', conn, if_exists='replace', index=False)
    
    conn.commit()
    conn.close()
    print(f"Loaded {len(df)} rows into {db_path}")

if __name__ == "__main__":
    load_csv_to_sqlite()
