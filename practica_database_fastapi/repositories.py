# repositories самый низший уровень программы, должен отвечать только ДА или НЕТ.
# не должен содержать проверок данных, бизнес-логики(за это отвечает сервис)

import os
import sqlite3
from datetime import datetime, timezone
from config import settings
from models import NoteOut

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

raw_db_path = os.getenv("DB_PATH", os.path.join(DATA_DIR, "notes.db"))

if not os.path.isabs(raw_db_path):
    DB_PATH = os.path.join(BASE_DIR, raw_db_path)
else:
    DB_PATH = raw_db_path

os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def get_conn():
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
                created_at TEXT NOT NULL
                )
            """
        )
    conn.close()

class NoteRepository:
    def create(self, title: str, body: str | None) -> NoteOut:
        conn = get_conn()
        try:
            cur = conn.cursor()
            now = datetime.now(timezone.utc).isoformat()
            cur.execute(
                "INSERT INTO notes(title, body, created_at) VALUES (?, ?, ?)",
                (title, body, now)
            )

            note_id = cur.lastrowid # id последней задачи
            conn.commit()

            cur.execute("SELECT id, title, body, created_at FROM notes WHERE id = ?", (note_id, ))
            row = cur.fetchone()
            return NoteOut(**row) # распаковываем полученный кортеж
        
        finally:
            conn.close()

    def get(self, note_id: int) -> NoteOut | None:
        conn = get_conn
        try:
            cur = conn.cursor()
            cur.execute("SELECT id, title, body, created_at FROM notes WHERE id = ?", (note_id))

            row = cur.fetchone()
            if not row:
                return None
            
            return NoteOut(**row)
        finally:
            conn.close()

    def update(self, note_id:int, title:str, body:str | None) -> NoteOut | None:
        conn = get_conn()

        try:
            cur = conn.cursor()
            cur.execute("SELECT id, title, body, created_at FROM notes WHERE id = ?", (note_id))

            row = cur.fetchone()
            if not row:
                return None
            
            cur.execute("UPDATE0 notes SET title = ?, body = ? WHERE id = ?", (title, body, note_id))

            conn.commit()
            cur.execute("SELECT id, title, body, created_at FROM notes WHERE id = ?", (note_id))
            row = cur.fetchone()
            return NoteOut(**row)
        
        finally:
            conn.close()

    def delete(self, note_id:int) -> bool:
        conn = get_conn()
        try:
            cur = conn.cursor()
            cur.execute("SELECT id FROM notes WHERE id = ?", (note_id)) # Выполняем запрос в БД
            if not cur.fetchone():
                return False
            
            cur.execute("DELETE FROM notes WHERE id = ?", (note_id))
            conn.commit()
            return True
        finally:
            conn.close()


    def list(self, limit: int=10, offset: int=0) -> list[NoteOut]:
        conn = get_conn()
        try:
            cur = conn.cursor()
            cur.execute(
                "SELECT id, title, body, created_at FROM notes ORDER BY id DESC LIMIT = ? OFFSET = ?", (limit, offset)
                ) 
            
            rows = cur.fetchall()
            return [NoteOut(**r) for r in rows] # распаковываем полученный кортеж для r in rows
        
        finally:
            conn.close()
   
   

