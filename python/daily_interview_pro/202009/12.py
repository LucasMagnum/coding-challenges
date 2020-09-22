"""
Palindrome Integers

This problem was recently asked by Twitter:

Given an integer, check if that integer is a palindrome.
For this problem do not convert the integer to a string to check if it is a palindrome.



"""

import math

def is_palindrome(n):
    if n == 0:
        return True
    k = int(math.log10(n))
    divisor = 10 ** k

    while n > 0:
        first_digit = n // divisor
        last_digit = n % 10

        if first_digit != last_digit:
            return False

        n = n % divisor
        n = n // 10
        divisor /= 100
  return True


if __name__ == "__main__":
    print(is_palindrome(1234321))
    # True
    print(is_palindrome(1234322))
    # False