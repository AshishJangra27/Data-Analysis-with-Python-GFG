"""
06_nested_models.py
Shows how to use nested Pydantic models.
"""
from pydantic import BaseModel

class Address(BaseModel):
    city: str
    zip_code: str

class Person(BaseModel):
    name: str
    address: Address

person = Person(name="Alice", address={"city": "NY", "zip_code": "10001"})
print(person)
