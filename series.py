"""Module will return the nth in both Fibonacci sequence and Lucas numbers."""


def fibonacci(n):
    """Function returns the nth number in the Fibonacci Sequence."""
    fibonacci_sequence = [0, 1]
    for x in range(0, n - 1):
        new = fibonacci_sequence[-2] + fibonacci_sequence[-1]
        fibonacci_sequence.append(new)
    return fibonacci_sequence[n - 1]


def lucas(n):
    """Get the nth number in the Lucas Numbers."""
    lucas_numbers = [2, 1]
    for x in range(0, n - 1):
        new = lucas_numbers[-2] + lucas_numbers[-1]
        lucas_numbers.append(new)
    return lucas_numbers[n - 1]


def sum_series(val, first=0, second=1):
    """Get the [value] number in a sequence of [first] and [second]."""
    series = [first, second]
    for x in range(0, val - 1):
        new = series[-2] + series[-1]
        series.append(new)
    return series[val - 1]

if __name__ == "__main__":  #pragma no cover
    print("This module defines functions that implement")
    print("mathematical series.\n")
    print("fibonacci(n):")
    print("\tReturns the nth value in the Fibonacci Sequence")
    print("fibonacci(5)")
    print("\t" + str(fibonacci(5)))
    print("\n")
    print("lucas(n):")
    print("\tReturns the nth value in the Lucas Numbers")
    print("lucas(5)")
    print("\t" + str(lucas(5)))
    print("\n")
    print("sum_series(n, first, second):")
    print("\tReturns the nth value in a sequence of numbers where the")
    print("\tnext number in a sequence is the sum of the last two numbers")
    print("\tThe first and second arguments are the first and second")
    print("\tnumbers in the sequence.")
    print("sum_series(3, 2, 3)")
    print("\t" + str(sum_series(3, 2, 3)))
