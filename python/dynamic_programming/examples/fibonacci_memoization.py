"""
Implementation of nth Fibonacci Number using Top-Down approach.
"""

import sys


def fibonacci(n):
    cache = {}

    def fib(n):
        if n <= 1:
            return n

        if n not in cache:
            cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]

    return fib(n)


if __name__ == "__main__":
    print(fibonacci(int(sys.argv[1])))
