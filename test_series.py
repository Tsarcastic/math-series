import pytest

"""This tests for the fifth number in the Fibonacci Sequence."""
def test_fibonacci01():
    from series import fibonacci
    assert fibonacci(5) == 3


"""This tests for the fifth item in the Lucas numbers."""
def test_lucas01():
    from series import lucas
    assert lucas(5) == 7


"""This tests for the fourth item in the sum series function. No value
    is entered for the first and second numbers in the sequence so it 
    defaults to the Fibonacci Sequence"""
def test_series01():
    from series import sum_series
    assert sum_series(4) == 2


"""This tests for the third number in the sequence that starts with two
    and three"""
def test_series02():
    from series import sum_series 
    assert sum_series(3, 2, 3) == 5