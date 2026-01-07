"""
04_default_values.py
Shows default values in Pydantic models.
"""
from pydantic import BaseModel

class Config(BaseModel):
    debug: bool = False
    timeout: int = 30

config = Config()
print(config)
