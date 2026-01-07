"""
08_functions.py
Shows Pythonic function definitions, default arguments, and *args/**kwargs.
"""

def greet(name, greeting="Hello"):
    """Greet a user with a message."""
    return f"{greeting}, {name}!"

# Use *args and **kwargs for flexible arguments

def print_args(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

print_args(1, 2, b=4)
