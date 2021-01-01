"""
Palindrome Integers

This problem was recently asked by Twitter:

Given an integer, check if that integer is a palindrome. 
For this problem do not convert the integer to a string to check if it is a palindrome.

"""

import math


def solution(number):
    if number == 0:
        return True

    k = int(math.log10(number))
    divisor = 10 ** k

    while number > 0:
        first_digit = number // divisor
        last_digit = number % 10

        if first_digit != last_digit:
            return False

        number = number % divisor
        number = number // 10
        divisor /= 100
    return True


if __name__ == "__main__":
    print(solution(1234321))
    print(solution(1234322))
