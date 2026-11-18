import sqlite3

DB_NAME = "database/events.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS events(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_type TEXT,
        timestamp TEXT,
        image_path TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_event(event_type, timestamp, image_path):

    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
    INSERT INTO events(event_type,timestamp,image_path)
    VALUES(?,?,?)
    """,
    (event_type, timestamp, image_path))

    conn.commit()
    conn.close()
