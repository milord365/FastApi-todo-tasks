from pydantic_settings import BaseSettings, SettingsConfigDict 

class Settings(BaseSettings):

    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30 

    APP_NAME: str 
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False 

    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding="utf-8",
        case_sensitive=True, 
        extra="ignore"
    )

settings = Settings()