"""
15_advanced_config.py
Demonstrates advanced Pydantic model configuration.
"""
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

    class Config:
        anystr_strip_whitespace = True
        min_anystr_length = 2

user = User(id=1, name="  Alice  ")
print(user)
