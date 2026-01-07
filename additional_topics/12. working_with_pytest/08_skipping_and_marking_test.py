
# Import pytest for skipping and marking tests
import pytest


# Mark this test as expected to fail
@pytest.mark.xfail(reason="Known bug")
def test_xfail():
    # This test is expected to fail
    assert 1 == 2

# Skip this test with a reason
@pytest.mark.skip(reason="Not implemented yet")
def test_skip():
    # This test will be skipped
    assert True



@pytest.mark.skip(reason="Not implemented yet")
def test_skips():
    # This test will be skipped
    assert True
