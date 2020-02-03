"""
    Add without Plus:

    Write a function that adds two numbers. You should not use + 
    or any arithemetic operators.
"""

import sys


def recursive_solution(a: int, b: int) -> int:
    if b == 0:
        return a
    
    total = a ^ b
    carry = (a & b) << 1

    return recursive_solution(total, carry)


def iterative_solution(a: int, b: int) -> int:
    while (b != 0):
        a, b = a ^ b, (a & b) << 1
    return a


if __name__ == "__main__":
    try:
        a, b = map(int, sys.argv[1:])
    except (IndexError, ValueError):
        a, b = 2, 4

    print(f"Sum ({a} + {b}) = ", recursive_solution(a, b))
