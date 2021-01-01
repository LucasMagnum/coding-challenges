"""
Reverse Integer

This problem was recently asked by LinkedIn:

Write a function that reverses the digits a 32-bit signed integer, x.
Assume that the environment can only store integers within the 32-bit signed integer range,
[-2^31, 2^31 - 1]. The function returns 0 when the reversed integer overflows.
"""


def solution(number):
    sign = 1 if number > 0 else -1
    reversed_str = sign * int(str(abs(number))[::-1])
    return reversed_str if -(2 ** 31) - 1 < reversed_str < 2 ** 31 else 0


if __name__ == "__main__":
    print(solution(123))
    print(solution(2 ** 31))
