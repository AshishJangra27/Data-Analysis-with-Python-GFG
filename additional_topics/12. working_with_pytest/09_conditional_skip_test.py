"""
10_conditional_skip.py
Skip test if .
"""
import os
import pytest

RUN_ADVANCED = False  # Set False to skip

@pytest.mark.skipif(not RUN_ADVANCED, reason="Advanced tests disabled")
def test_env_skip():
    assert True
