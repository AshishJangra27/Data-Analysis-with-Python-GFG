
# Import Mock from unittest.mock for mocking objects
from unittest.mock import Mock


# Test using a mock object
def test_mocking():
    # Create a mock object
    mock = Mock()
    # Set the return value of the mock
    mock.return_value = 42
    # Assert that calling the mock returns 42
    assert mock() == 42
