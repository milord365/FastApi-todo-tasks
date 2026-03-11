from repositories import NoteRepository
from models import NoteOut
from typing import Optional

class NoteService():
    def __init__(self, repo: NoteRepository):
        self.repo = repo

    def create_note(self, title: str, body: str | None) -> NoteOut: # body:Optional[str]
        if not title or not title.strip():
            raise ValueError("title_empty")
       
        return self.repo.create(title=title, body=body)
    
    def get_note(self, note_id: int) -> Optional[NoteOut]:
        return self.repo.get(note_id)
    

    def list_notes(self, limit: int=10, offset: int=0) -> list[NoteOut]:
        return self.repo.list(limit=limit, offset=offset)


    def update_note(self, note_id: int, title: str, body: Optional[str]) -> Optional[NoteOut]:
        if not title or not title.strip():
            raise ValueError("title_empty")
       
        return self.repo.update(note_id=note_id, title=title, body=body)
    
    def delete_note(self, note_id: int) -> bool:
        return self.repo.delete(note_id)
    

    