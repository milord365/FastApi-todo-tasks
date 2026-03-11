from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from repositories import init_db
from routers import router as notes_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="Practice01", lifespan=lifespan)
# Ловим все ошибки и выводим в консоль
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    print("=" * 50)
    print(f"ERROR on {request.method} {request.url}")
    traceback.print_exc()  # Полный traceback в терминал
    print("=" * 50)
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)}  # Покажет текст ошибки в Swagger
    )
app.include_router(notes_router)

# uvicorn app:app --reload запуск приложения
# python -m uvicorn app:app --reload