import os
from pydantic_settings import BaseSettings
from pydantic import ConfigDict

BASE_DIR = os.path.dirname(__file__)
DEFAULT_DB = os.path.join(BASE_DIR, "data", "notes.db")

class Settings(BaseSettings):
    DB_PATH: str = DEFAULT_DB #путь до базы данных

    model_config = ConfigDict(
        env_file = os.path.join(BASE_DIR, ".env"),
        env_file_encoding = "utf-8"
    )

settings = Settings()