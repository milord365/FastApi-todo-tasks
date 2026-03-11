from fastapi import FastAPI
from database import engine
import models
from routers import products, students

# создает таблицу в бд
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="University API")

# подключает роутер
app.include_router(products.router)
app.include_router(students.router)

@app.get("/")
def root():
    return {"message": "Здарова в API"}