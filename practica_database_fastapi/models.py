from pydantic import BaseModel

class NoteOut(BaseModel):
    id: int
    title: str
    body: str | None
    created_at: str

class NoteCreate(BaseModel):
    title: str
    body: str = ""