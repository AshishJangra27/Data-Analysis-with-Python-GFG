"""
10_error_handling.py
Demonstrates error handling and validation errors in Pydantic.
"""
from pydantic import BaseModel, ValidationError

class Item(BaseModel):
    name: str
    price: float

try:
    item = Item(name="Book", price="not_a_float")
    
except ValidationError as e:
    print("Validation error:", e)
