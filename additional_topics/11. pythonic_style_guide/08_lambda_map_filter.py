"""
12_lambda_map_filter.py
Shows Pythonic use of lambda, map, and filter.
"""

# Lambda functions for short, simple operations
add = lambda x, y: x + y
print(add(2, 3))

# Use map to apply a function to a sequence
numbers = [1, 2, 3]
squared = list(map(lambda x: x**2, numbers))
print(squared)

# Use filter to select items from a sequence
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
