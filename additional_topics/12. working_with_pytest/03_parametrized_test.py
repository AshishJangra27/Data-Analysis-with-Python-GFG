
# Import pytest for using parametrize
import pytest


# Parametrized test to check addition for multiple values
@pytest.mark.parametrize("a,b,result", [
    (1, 2, 3),  # 1 + 2 = 3
    (2, 3, 5),  # 2 + 3 = 5
    (3, 4, 7),   # 3 + 4 = 7
    (5, 7, 12),  # 5 + 7 = 12
    (10, 15, 25), # 10 + 15 = 25
    (0, 0, 0)    # 0 + 0 = 0
])
def test_add(a, b, result):
    # Assert that a + b equals result
    assert a + b == result
