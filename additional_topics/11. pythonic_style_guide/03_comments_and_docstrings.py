"""
03_comments_and_docstrings.py
Demonstrates Pythonic commenting and docstring practices.
"""

# Use comments to explain why, not what
x = 42  # Chosen as the answer to everything

# Use docstrings for modules, classes, and functions

def calculate_area(radius):
    """Calculate the area of a circle given its radius."""
    import math
    return math.pi * radius ** 2

class Circle:
    """Represents a circle shape."""
    def __init__(self, radius):
        self.radius = radius
