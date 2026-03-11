from typing import Optional
from app.security.auth import get_password_hash
from app.repository.schemas import UserInDB

class UserRepository:
    def __init__(self):
        self._users: dict[str, UserInDB] = {
            "admin": UserInDB(
                username="admin",
                email="admin@example.com",
                full_name="Maxim_admin",
                hashed_password=get_password_hash("admin123"),
                disabled=False
            ),
            "user": UserInDB(
                username="user",
                email="user@example.com",
                full_name="Regular user",
                hashed_password=get_password_hash("user123"),
                disabled=False
            )
        }

    def get_user_by_username(self, username: str) -> Optional[UserInDB]:
        return self._users.get(username)

    def create_user(self, user: UserInDB) -> UserInDB:
        if user.username in self._users:
            raise ValueError(f"user {user.username} already exists")

            self._users[user, username] = user
            return user

    def user_exists(self, username: str) -> bool:
        return username in self._users

user_repository = UserRepository()

    