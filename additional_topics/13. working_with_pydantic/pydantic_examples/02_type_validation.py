"""
02_type_validation.py
Shows automatic type validation in Pydantic models.
"""
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    price: float

product = Product(id="2", price="19.99")  # Pydantic will coerce types
print(product)
