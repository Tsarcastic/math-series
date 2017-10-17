"""Get the nth number in a sequence."""


"""Get the nth number in the Fibonacci Sequence"""


def fibonacci(n):
    fibonacci_sequence = [0, 1]
    #n = int(input('Which number in the Fibonacci Sequence?'))
    for x in range(0, n - 1):
        new = fibonacci_sequence[-2] + fibonacci_sequence[-1]
        fibonacci_sequence.append(new)
    #print(fibonacci[n - 1] + " is the " + n + "th # in the Sequence")


"""Get the nth number in the Lucas Numbers"""


def lucas(n):
    lucas_numbers = [2, 1]
    #n = int(input('Which number in the Lucas Numbers?'))
    for x in range(0, n - 1):
        new = lucas_numbers[-2] + lucas_numbers[-1]
        lucas_numbers.append(new)
    #print(lucas[n - 1] + " is the " + n + "th # in the Numbers")

def sum_series(val, first=0, second=1):
       if (first == 0) and (second == 1):
        return fibonacci(val):

