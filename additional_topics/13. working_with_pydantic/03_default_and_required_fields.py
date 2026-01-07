
"""
03_default_and_required_fields.py
Demonstrates default values and required fields in Pydantic.

This program shows how to use required and default fields in a Pydantic model:
1. Required fields must be provided when creating an instance.
2. Fields with default values are optional and get their default if not provided.
"""

# Import the BaseModel class from pydantic
from pydantic import BaseModel


class Book(BaseModel):
    title: str              # Book title (required)
    author: str = "Unknown" # Author name (default: "Unknown")
    pages: int = 100        # Number of pages (default: 100)

book1 = Book(title="Python 101")
print(book1)

book2 = Book(title="Advanced Python", author="John Doe", pages=350)
print(book2)

# ---
# Summary:
# This program demonstrates how Pydantic models handle required and default fields.
# You must provide required fields, while optional fields use their default values if not given.
