
# Import pytest for exception testing
import pytest


# Function to perform division
def divide(a, b):
    return a / b


# Test that division by zero raises ZeroDivisionError
def test_zero_division():
    # Use pytest.raises to check for exception
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
