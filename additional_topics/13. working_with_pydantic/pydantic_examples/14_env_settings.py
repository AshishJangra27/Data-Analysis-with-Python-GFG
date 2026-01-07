"""
14_env_settings.py
Shows how to use Pydantic's BaseSettings for environment variables.
"""
from pydantic_settings import BaseSettings
import os

os.environ["API_KEY"] = "secret-key"

class Settings(BaseSettings):
    api_key: str

settings = Settings()
print(settings)
