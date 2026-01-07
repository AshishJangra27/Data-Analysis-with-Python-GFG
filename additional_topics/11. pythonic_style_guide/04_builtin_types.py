"""
04_builtin_types.py
Shows Pythonic usage of built-in types: lists, dicts, sets, and tuples.
"""

# Use list comprehensions for concise list creation
squares = [x**2 for x in range(10)]

# Use dict comprehensions
square_dict = {x: x**2 for x in range(5)}

# Use sets for unique items
unique_names = {"Alice", "Bob", "Alice"}  # {'Alice', 'Bob'}

# Use tuples for immutable groups of items
point = (3, 4)
