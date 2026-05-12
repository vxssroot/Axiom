from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True, extra="ignore")

    ENVIRONMENT: Literal["development", "staging", "production"] = "development"
    DEBUG: bool = True
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    CORS_ORIGINS: list[str] = ["http://localhost:3000", "http://localhost:3001"]

    # Database
    POSTGRES_URL: str = "postgresql+psycopg://postgres:postgres@localhost:5432/axiom"

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # GitHub App (placeholders)
    GITHUB_APP_ID: str | None = None
    GITHUB_APP_PRIVATE_KEY: str | None = None

settings = Settings()
