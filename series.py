"""Get the nth number in a sequence."""


"""Get the nth number in the Fibonacci Sequence"""


def fibonacci():
    fibonacci = [0, 1]
    n = int(input('Which number in the Fibonacci Sequence?'))
    for x in range(0, n - 1):
        new = fibonacci[-2] + fibonacci[-1]
        fibonacci.append(new)
    print(fibonacci[n - 1] + " is the " + n + "th # in the Sequence")


"""Get the nth number in the Lucas Numbers"""


def lucas():
    lucas = [2, 1]
    n = int(input('Which number in the Lucas Numbers?'))
    for x in range(0, n - 1):
        new = lucas[-2] + lucas[-1]
        lucas.append(new)
    print(lucas[n - 1] + " is the " + n + "th # in the Numbers")


fibonacci()
lucas()


