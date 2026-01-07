"""
12_parametrized_fixture.py
Parametrized fixture with indirect parametrization.
"""
import pytest

@pytest.fixture
def number(request):
    # request.param allows the fixture to receive values from @pytest.mark.parametrize.
    return request.param

@pytest.mark.parametrize("number", [10, 20,30,40,32,42], indirect=True)
def test_number_is_even(number):
    assert number % 2 == 0


# Tells pytest to run the test twice, once with number=10 and once with number=20.
# indirect=True means the value is passed to the fixture, not directly to the test function.

