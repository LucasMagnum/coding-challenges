"""
Perfect Number

This problem was recently asked by Facebook:

A Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

For instance,
28 = 1 + 2 + 4 + 7 + 14

Write a function to determine if a number is a perfect number.

"""

import functools
import math


def solution(num):
    factors = []

    if num <= 0:
        return False

    for i in range(1, int(math.ceil(num ** 0.5))):
        if num % i == 0:
            factors.append(i)
            factors.append(num / i)

    total = 0
    if factors:
        total = functools.reduce(lambda x, y: x + y, factors) - num
        return total == num

if __name__ == "__main__":
    print(solution(28))
    # True
    # 28 = 1 + 2 + 4 + 7 + 14