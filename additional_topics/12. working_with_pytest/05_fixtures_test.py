
# Import pytest for usperfecting fixtures
import pytest


# Define a fixture that returns a sample list
@pytest.fixture
def sample_list():
    # Return a list of numbers
    return [1, 2, 3]


# Test using the fixture sample_list
def test_sum(sample_list):
    # Assert that the sum of the sample list is 6
    assert sum(sample_list) == 6
