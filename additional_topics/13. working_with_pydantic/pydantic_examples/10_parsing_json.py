"""
10_parsing_json.py
Shows parsing JSON data into Pydantic models.
"""
from pydantic import BaseModel
import json

class Animal(BaseModel):
    type: str
    age: int

json_data = '{"type": "dog", "age": 5}'
animal = Animal.parse_raw(json_data)
print(animal)
