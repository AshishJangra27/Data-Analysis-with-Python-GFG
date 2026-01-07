"""
08_validators.py
Shows custom validation using @validator.
"""
from pydantic import BaseModel, validator

class User(BaseModel):
    name: str
    age: int

    @validator('age')
    def age_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Age must be positive')
        return v

user = User(name="Alice", age=25)
print(user)
