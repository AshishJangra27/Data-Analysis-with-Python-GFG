
from pydantic import BaseModel

# Define a simple model called 'User' with two fields:

class User(BaseModel):
    name: str  # The user's name
    age: int   # The user's age

user = User(name="Alice", age=True)

print(user)

print("Name:", user.name)
print("Age:",  user.age)