"""
05_unpacking.py
Demonstrates Pythonic unpacking of sequences and dictionaries.
"""

# Unpacking lists/tuples
x, y = (1, 2)

# Extended unpacking
first, *rest = [1, 2, 3, 4]
print(first,'|',rest)

# Unpacking in loops
pairs = [(1, 'a'), (2, 'b')]

for number, letter in pairs:
    print(f"Number: {number}, Letter: {letter}")

# Unpacking dictionaries
person = {'name': 'Alice', 'age': 30}
name, age = person.values()
