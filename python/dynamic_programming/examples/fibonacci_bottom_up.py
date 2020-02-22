"""
Implementation of nth Fibonacci Number ussing a Bottom-Up approach.
"""

import sys


def fibonacci(n):
    if n == 0:
        return 0

    a, b = 0, 1

    for i in range(2, n):
        a, b = b, a + b

    return a + b


if __name__ == "__main__":
    print(fibonacci(int(sys.argv[1])))
