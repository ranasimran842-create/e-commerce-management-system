import sqlite3


def connect_db():
    return sqlite3.connect("ecommerce.db")


def create_table():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        category TEXT,
        price INTEGER,
        quantity INTEGER
    )
    """)

    conn.commit()
    conn.close()