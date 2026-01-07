"""
12_custom_types_and_constraints.py
Demonstrates custom types and constraints in Pydantic.
"""
from pydantic import BaseModel, constr, conint, EmailStr

class User(BaseModel):
    username: constr(min_length=3, max_length=20)
    age: conint(gt=18, lt=110)
    email: EmailStr

user = User(username="alice123", age=27, email="a@b.in")
print(user)
