import os
from pydantic_settings import BaseSettimgs
from pydantic import ConfigDict

BASE_DIR = os.path.dirname(__file__)
DEFAULT_DB = os.path.join(BASE_DIR, "data", "notes.db")

class Settings(BaseSettimgs):
    DB_PATH: str = DEFAULT_DB

    model_config = ConfigDict(
        env_file = os.path.join(BASE_DIR, ".env"),
        env_file_encoding = "utf-8"
    )


    Settings = Settings()