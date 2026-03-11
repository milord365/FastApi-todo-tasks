import bcrypt 
from datetime import datetime, timdelta, timezone 
from typing import Optional
from jose import JWTError, ExpiredSignatureError, jwt 
from fastapi import Depends, HTTPException, status 
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials 

from app.configs import settings 

security_scheme = HTTPBearer()

def get_password_pash(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)

    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))



