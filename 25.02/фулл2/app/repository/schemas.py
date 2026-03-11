from typing import Optional
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    hashed_password: str
    disabled: bool = False

class UserInDB(User):
    pass

class UserInDB(User):
    pass

class UserResponse(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    disabled: bool = False

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: int

class LoginRequiest(BaseModel):
    username: str
    password: str


