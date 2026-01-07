
"""
05_optional_and_missing_fields.py
Demonstrates handling of Optional and missing fields in Pydantic.

This program shows how to use optional fields in a Pydantic model:
1. Optional fields can be left out when creating an instance.
2. If not provided, they get their default value (usually None).
"""

from typing import Optional
from pydantic import BaseModel

class Profile(BaseModel):
    username: str              # The user's username (required)
    bio: Optional[str] = None  # The user's bio (optional)


profile1 = Profile(username="coder")
print(profile1)

profile2 = Profile(username="dev", bio="Python enthusiast")
print(profile2)

# ---
# Summary:
# This program demonstrates how to use optional fields in Pydantic models.
# Optional fields can be omitted, and will default to None or another value if not provided.
