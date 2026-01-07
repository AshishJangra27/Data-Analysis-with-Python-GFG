"""
05_optional_fields.py
Demonstrates optional fields using typing.Optional.
"""
from pydantic import BaseModel
from typing import Optional

class Profile(BaseModel):
    username: str
    bio: Optional[str] = None

profile = Profile(username="bob")
print(profile)
