"""
11_model_inheritance.py
Demonstrates inheritance in Pydantic models.
"""
from pydantic import BaseModel

class BaseUser(BaseModel):
    id: int

class AdminUser(BaseUser):
    admin_level: int

admin = AdminUser(id=1, admin_level=5)
print(admin)
