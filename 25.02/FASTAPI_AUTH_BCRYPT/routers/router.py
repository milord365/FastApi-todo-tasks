from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel

from app.services.user_service import auth_service, user_service
from app.repository import UserResponse
from app.repository.schemas import TokenResponse, LoginRequest
from app.security.auth import get_current_user_username


auth_router = APIRouter(prefix="/auth", tags=["Authentication"])

@auth_router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
async def login(request: LoginRequest):
        token_data = auth_service.authenticate_user(request.username, request.password)

        if not token_data:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"}
            )
        
        return TokenResponse(**token_data)


user_router = APIRouter(prefix="/users", tags=["Users"])

@user_router.get("/me", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def get_current_user(username: str = Depends(get_current_user_username)):
    user = user_service.get_user_by_username(username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user
