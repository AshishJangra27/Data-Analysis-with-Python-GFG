"""
02_code_layout.py
Shows Pythonic code layout: indentation, line length, blank lines, and imports.
"""

# Use 4 spaces per indentation level
for i in range(3):
    print(i)

# Limit lines to 79 characters
long_string = "This is a long string, but it should not exceed 79 characters in a line."

# Use blank lines to separate functions and classes

def foo():
    pass

class Bar:
    pass

# Imports should be on separate lines and at the top
import os
import sys
