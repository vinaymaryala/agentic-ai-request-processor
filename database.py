import sqlite3
from datetime import datetime

DB_NAME = "data/logs.db"


def init_db():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS requests (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        request TEXT,

        category TEXT,

        urgency TEXT,
        
        confidence INTEGER,

        assigned_team TEXT,

        status TEXT,

        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_request(
    request,
    category,
    urgency,
    confidence,
    assigned_team,
    status
):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO requests
        (
            request,
            category,
            urgency,
            confidence,
            assigned_team,
            status,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            request,
            category,
            urgency,
            confidence,
            assigned_team,
            status,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    )

    conn.commit()

    conn.close()


def get_requests():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM requests
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows