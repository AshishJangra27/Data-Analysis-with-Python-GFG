"""
09_aliases.py
Demonstrates field aliases in Pydantic models.
"""
from pydantic import BaseModel, Field

class Car(BaseModel):
    model: str = Field(..., alias="car_model")
    year: int

car = Car(car_model="Tesla", year=2022)
print(car)
