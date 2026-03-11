from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.configs import settings
from app.routers.router import auth_router, user_router
import uvicorn

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description= "API с Bearer-аутентификацией"
)

app.include_router(auth_router)
app.include_router(user_router)

@app.get("/", tags=["Root"])
async def root():
    return JSONResponse(
        content = {
            "message": "User Authentication API",
            "version": settings.APP_VERSION,
            "docs": "/docs",
            "endpoints": {
                "login": "POST /auth/login",
                "current_user": "GET /users/me"
            }
        }
    )


@app.get("/health", tags=["Health"])
async def health_check():
    return JSONResponse(
        content = {
            "status": "healthy",
            "version": settings.APP_VERSION
        }
    )





