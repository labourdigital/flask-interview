import sqlite3


# Function to set up the database and populate it with sample data
def setup_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        country TEXT
    )"""
    )

    # Insert sample data if the table is empty
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            """
        INSERT INTO users (name, email, region) VALUES (?, ?, ?)
        """,
            [
                ("Alice", "alice@example.com", "North West"),
                ("Bob", "bob@example.com", "London"),
                ("Charlie", "charlie@example.com", "East Midlands"),
                ("David", "david@example.com", "London"),
                ("Eve", "eve@example.com", "South East"),
                ("Frank", "frank@example.com", "South West"),
                ("Grace", "grace@example.com", "North West"),
                ("Hank", "hank@example.com", "Yorkshire and  Humber"),
                ("Ivy", "ivy@example.com", "North West"),
                ("Jack", "jack@example.com", "West Midlands"),
            ],
        )
    conn.commit()
    conn.close()
