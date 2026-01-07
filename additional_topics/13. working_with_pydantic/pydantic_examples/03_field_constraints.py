"""
03_field_constraints.py
Demonstrates field constraints using Pydantic's Field.
"""
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    quantity: int = Field(..., ge=1, le=100)

item = Item(name="Book", quantity=10)
print(item)
