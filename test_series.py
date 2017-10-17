import pytest


def test_fibonacci01():
    from series import fibonacci
    assert fibonacci(5) == 3

def test_lucas01():
    from series import lucas
    assert lucas(5) == 7

def test_series01():
    from series import sum_series
    assert sum_series(4) == 2

def test_series02():
    from series import sum_series 
    assert sum_series(3, 2, 3) == 5