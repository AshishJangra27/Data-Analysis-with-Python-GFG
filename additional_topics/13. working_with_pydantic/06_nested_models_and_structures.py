"""
08_nested_models_and_structures.py
Demonstrates nested models and complex data structures.
"""
from typing import List
from pydantic import BaseModel

class Address(BaseModel):
    city: str
    zip: str

class User(BaseModel):
    name: str
    addresses: List[Address]
    

user = User(name="Alice", addresses=[Address(city="NY", zip="10001"),
                                     Address(city="LA", zip="90001")])
print(user)
