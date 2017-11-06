"""Test the series."""


def test_fibonacci01():
    """Will test for the fifth number in the Fibonacci Sequence."""
    from series import fibonacci
    assert fibonacci(5) == 3


def test_fiboncacci_at_7():
    """Will test for the 7th number in the sequence."""
    from series import fibonacci
    assert fibonacci(7) == 8


def test_lucas01():
    """Will test for the fifth item in the Lucas numbers."""
    from series import lucas
    assert lucas(5) == 7


def test_series01():
    """Will test that sum series defaults to fibonacci."""
    from series import sum_series
    assert sum_series(4) == 2


def test_series02():
    """Will test for the third number in the sequence that starts with two and three."""
    from series import sum_series
    assert sum_series(3, 2, 3) == 5
