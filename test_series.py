import pytest


def test_fibonacci01():
    """This tests for the fifth number in the Fibonacci Sequence."""
    from series import fibonacci
    assert fibonacci(5) == 3


def test_lucas01():
    """This tests for the fifth item in the Lucas numbers."""
    from series import lucas
    assert lucas(5) == 7



def test_series01():
    """This tests for the fourth item in the sum series function. No value
    is entered for the first and second numbers in the sequence so it 
    defaults to the Fibonacci Sequence"""
    from series import sum_series
    assert sum_series(4) == 2



def test_series02():
    """This tests for the third number in the sequence that starts with two
    and three"""
    from series import sum_series 
    assert sum_series(3, 2, 3) == 5
