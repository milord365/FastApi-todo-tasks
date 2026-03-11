from fatsapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime, timezone

app = FastAPI(title="ToDo v2 (in-memory)")

def now_utc() -> datetime:
    return datetime.now(timezone.utc)

class Store:
    def __init__(self) -> None:
        self._lock = asyncio.Lock()
        self._users: dict[int, dict] = {}
        self._tasks: dict[int, dict] = {}
        self._task_id_seq = 0
        self._user_id = 0

async def create_task(self, owner_id: int, title: str, description: str | None) -> dict:
    async with self._lock:
        tasks = list(sel)
        if owner_id not in self._users:
            return KeyError("owner_id")