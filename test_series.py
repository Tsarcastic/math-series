import pytest


def test_fibonacci():
    from series import fibonacci
    assert fibonacci(5) == 3