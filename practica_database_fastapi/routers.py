from fastapi import APIRouter, HTTPException, status, Depends
from models import NoteCreate, NoteOut
from services import NoteService
from repositories import NoteRepository

router = APIRouter(prefix="/notes", tags=["notes"]) # prefix  для того чтобы не писать постоянно notes, будет заполнятся автоматически

def get_service():
    repo = NoteRepository()
    return NoteService(repo)

@router.post("", response_model=NoteOut, status_code=status.HTTP_201_CREATED) # post - отправить запрос, response_model=NoteOut - проверка ответа
def create_note(payload: NoteCreate, service: NoteService = Depends(get_service)): # payload - полезная нагрузка, NoteCreate -  отсекает лишнее, Depends(зависимость) вызовет метод и вернет объект экземпляра класса (вернется NoteService(repo))
    try:
        return service.create_note(payload.title, payload.body) # payload.title, payload.body связано с paydantic, почитать про это (принимает json объект, а возвращает объект класса)
    except ValueError:
        raise HTTPException(status_code=422, detail={"error": "Validation", "reason": "title_empty"})
    

@router.get("/{note_id}", response_model=NoteOut)
def get_note(note_id: int, service: NoteService = Depends(get_service)):
    note = service.get_note(note_id)

    if not note:
        raise HTTPException(status_code=404, detail={"error": "Not Found", "reason": "note_not_found"})
    
    return note

@router.get("/", response_model=NoteOut)                                                            # get-запрос
def list_notes(limit: int=10, offset: int=0, service: NoteService = Depends(get_service)):
    if limit < 0 or offset < 0:
        raise HTTPException(status_code=400, detail={"error": "Bad Request"})
    
    return service.list_notes(limit=limit, offset=offset)

@router.patch("/{note_id}", response_model=NoteOut)                                                # patch-обновление
def patch_note(note_id: int, payloud: NoteCreate, service: NoteService = Depends(get_service)):
    try:
        note = service.update_note(note_id, payloud.title, payloud.body)
    except ValueError:
        raise HTTPException(status_code=422, detail={"error": "Validation", "reason": "title_empty"})
    
    if not note:
        raise HTTPException(status_code=404, detail={"error": "Not Found", "reason": "note_not_found"})
    return note

@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)                               # delete-удаление
def delete_note(note_id: int, service: NoteService = Depends(get_service)):
    ok = service.delete_note(note_id)
    if not ok:
        raise HTTPException(status_code=404, detail={"error": "Not Found", "reason": "note_not_found"})
    
    return None