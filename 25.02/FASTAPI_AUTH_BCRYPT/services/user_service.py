from typing import Optional
from datetime import timedelta

from app.repository import user_repository, userResponse
from app.configs import settings
from app.security import verify_password, create_access_token

class AuthService:
    def __init__(self):
        self.user_repo = user_repository


    def authenticate_user(self, username: str, password: str) -> Optional[dict]:
        user = self.user_repo.get_user_by_username(username)

        if not user:
            return None
        if not verify_password(password, user.hashed_password):

        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username},
            expires_delta=access_token_expires
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
        }
    
    class UserService:
        def __init__(self):
            self.user_repo = user_repository

        def get_user_by_username(self, username: str) -> Optional[UserResponse]:
            user = self.user_repo.get_user_by_username(username)

        if not user:
            return None

        if user.disabled:
            return None

        return UserResponse(
            username=user.username,
            email=user.email,
            full_name=user.full_name,
            disabled=user.disabled
        )