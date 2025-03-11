import sqlite3
import pandas as pd

def get_data():
    df = pd.read_csv('january_transactions.csv', parse_dates=['Campaign Date'], dayfirst=True)
    return df
            
# Function to set up the database and populate it with sample data
def setup_db():
    conn = sqlite3.connect("transactions.db")
    cursor = conn.cursor()
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        supporter_id INTEGER,
        amount FLOAT,
        date DATE,
        region TEXT
    )"""
    )
    data = get_data()

    # Insert sample data if the table is empty
    cursor.execute("SELECT COUNT(*) FROM transactions")
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            """
        INSERT INTO transactions (supporter_id, amount, date, region) VALUES (?, ?, ?, ?)
        """,
            [
                (
                    row['Supporter ID'],
                    row['Amount'],
                    row['Campaign Date'],
                    row['region']
                )
                for i, row in data.iterrows()
            ],
        )
    conn.commit()
    conn.close()
