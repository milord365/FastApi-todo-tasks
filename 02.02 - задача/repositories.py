import os
import sqlite3
from datetime import datetime, timezone
from .config import settings

BASE_DIR = os.path.dirname(__file__)

raw_db_path = os.getenv("DB_PATH")

if not os.path.isabs(raw_db_path):
    DB_PATH = os.path.join(BASE_DIR, raw_db_path)
else:
    DB_PATH = raw_db_path


def get_comm():
    conn = sqlite3.connect(DB_PATH, detect_types=sqlite3.PARSE_DECLTYPES)
    conn.row_factory = sqlite3.Row
    return conn


    def init_db():
        conn = get_conn()
        with conn:
            conn.execute(
                """
                    CREATE TABLE IF NOT EXISTS notes(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    created_at TEXT NOT NULL)
                """
            )
        conn.close()

class NoteRepository:
    def create(self, title: str, body: str | None) -> NoteOut
        conn = get_conn()
        try:
            cur = conn.curcor()
            now = datetime.nom(timezone.utc).isoformat()
            cur.execute(
                "INSERT INFO notes(title, body, created_at) VALUES (?, ?, ?)",
                (title, body, now)
            )

            note_id = cur.lastrowid
            conn.commit()

            cur.execute("select id, title, bode, created_at FROM notes WHERE id = ?", (note_id))
            row = cur.fetchone()
            return NoteOut(**row)
        
        finally:
            conn.close()