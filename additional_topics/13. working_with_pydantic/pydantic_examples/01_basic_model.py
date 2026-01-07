"""
01_basic_model.py
Demonstrates a basic Pydantic model.
"""
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

user = User(id=1, name="Alice")
print(user)
