from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "Store API"
    ROOT_PATH: str = "/"
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
