
"""
06_model_methods_and_repr.py
Demonstrates adding methods and customizing model representation.

This program shows how to add custom methods and string representation to a Pydantic model:
1. You can define methods (like area) for your model.
2. You can customize how the model prints by overriding __str__.
"""

# Import the BaseModel class from pydantic
from pydantic import BaseModel


class Rectangle(BaseModel):

    width: float   # The rectangle's width
    height: float  # The rectangle's height

    # Method to calculate the area of the rectangle
    def area(self) -> float:
        return self.width * self.height

    # Custom string representation for the model
    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"


rect = Rectangle(width=5, height=3)

print(rect)

print('---')
print("Area:", rect.area())

# ---
# Summary:
# This program demonstrates how to add custom methods and string output to Pydantic models.
# You can use models like regular Python classes, with your own logic and formatting.
