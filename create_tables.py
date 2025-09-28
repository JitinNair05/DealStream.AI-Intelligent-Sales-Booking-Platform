# create_tables.py
import sqlite3
from pathlib import Path

DB = "sales_ai.db"

schema = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE,
    name TEXT,
    stage TEXT,
    reg_date TEXT
);

CREATE TABLE IF NOT EXISTS calls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    bot TEXT,
    transcript TEXT,
    outcome TEXT,
    call_time TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    payload TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    slot_date TEXT,
    slot_time TEXT,
    status TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
"""

def main():
    db_path = Path(DB)
    conn = sqlite3.connect(DB)
    try:
        conn.executescript(schema)
        conn.commit()
        print(f"Database initialized at: {db_path.resolve()}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
