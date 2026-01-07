"""
11_inheritance_and_composition.py
Demonstrates inheritance and model composition in Pydantic.
"""
from pydantic import BaseModel

class Animal(BaseModel):
    name: str

class Dog(Animal):
    breed: str

class Owner(BaseModel):
    name: str
    pet: Animal

owner = Owner(name="Sam", pet=Dog(name="Rex", breed="Labrador"))
print(owner)
