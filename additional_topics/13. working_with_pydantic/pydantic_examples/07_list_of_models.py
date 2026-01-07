"""
07_list_of_models.py
Demonstrates lists of Pydantic models.
"""
from pydantic import BaseModel
from typing import List

class Tag(BaseModel):
    name: str

class Blog(BaseModel):
    title: str
    tags: List[Tag]

blog = Blog(title="My Blog", tags=[{"name": "python"}, {"name": "pydantic"}])
print(blog)
