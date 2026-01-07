"""
01_naming_conventions.py
Demonstrates Pythonic naming conventions for variables, functions, classes, and constants.
"""

# Variable names should be lowercase with words separated by underscores
user_name = "Alice"  # Good
username = "Bob"     # Acceptable
UserName = "Charlie" # Not recommended

# Function names should be lowercase with underscores

def get_user_age():
    """Return a user's age."""
    return 30

# Class names should use CapWords convention

class UserProfile:
    def __init__(self, name):
        self.name = name

# Constants should be all uppercase
MAX_USERS = 100

# Document your code with docstrings and comments
