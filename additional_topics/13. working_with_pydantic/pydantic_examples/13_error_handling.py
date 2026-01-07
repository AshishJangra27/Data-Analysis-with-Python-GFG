"""
13_error_handling.py
Demonstrates error handling in Pydantic models.
"""
from pydantic import BaseModel, ValidationError

class Fruit(BaseModel):
    name: str
    quantity: int

try:
    fruit = Fruit(name="Apple", quantity="ten")
except ValidationError as e:
    print(e)
