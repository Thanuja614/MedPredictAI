"""
MedPredict AI — Application Configuration
Loads application settings from environment variables and .env file.
"""

import os
from pathlib import Path
from typing import List, Union
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent

class Settings(BaseSettings):
    # Application Identity
    APP_NAME: str = "MedPredict AI"
    APP_ENV: str = "development"
    APP_DEBUG: bool = True
    API_V1_STR: str = "/api/v1"
    PROJECT_VERSION: str = "1.0.0"

    # Security & Cryptography
    SECRET_KEY: str = "medpredict_dev_secret_key_change_in_production_super_secure_32_bytes"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # Database Configuration
    DATABASE_URL: str = "postgresql+psycopg://medpredict_user:medpredict_pass@localhost:5432/medpredict_db"
    DATABASE_TEST_URL: str = "sqlite:///./test_medpredict.db"
    DB_POOL_SIZE: int = 10
    DB_MAX_OVERFLOW: int = 20
    DB_ECHO: bool = False

    # Cache & Queue Configuration (Redis)
    REDIS_URL: str = "redis://localhost:6379/0"
    CACHE_ENABLED: bool = True
    CACHE_TTL_SECONDS: int = 3600

    # CORS Origins
    BACKEND_CORS_ORIGINS: Union[List[str], str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]

    # Medical Safety & Risk Classification
    SYSTEM_DISCLAIMER_ENFORCED: bool = True
    RISK_THRESHOLD_MODERATE: float = 0.35
    RISK_THRESHOLD_HIGH: float = 0.70

    # Storage & Directories
    STORAGE_LOCAL_ROOT: str = str(ROOT_DIR / "storage")
    DATASETS_DIR: str = str(ROOT_DIR / "data" / "datasets")
    MODELS_DIR: str = str(ROOT_DIR / "models" / "artifacts")
    REPORTS_DIR: str = str(ROOT_DIR / "reports" / "generated")

    # Observability
    LOG_LEVEL: str = "INFO"
    RATE_LIMIT_PER_MINUTE: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        case_sensitive=True
    )

settings = Settings()
