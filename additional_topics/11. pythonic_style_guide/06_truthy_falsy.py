"""
06_truthy_falsy.py
Shows Pythonic ways to use truthy and falsy values in conditions.
"""

# Use direct truthy/falsy checks
items = []
if not items:
    print("No items!")

# Avoid explicit comparisons to True/False/None
flag = None
if flag is None:
    print("Flag is None")
