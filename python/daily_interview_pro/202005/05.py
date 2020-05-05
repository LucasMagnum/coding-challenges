"""
Plus One

This problem was recently asked by LinkedIn:

Given a non-empty array where each element represents a digit of a non-negative integer
add one to the integer. The most significant digit is at the front of the array and each element
in the array contains only one digit.

Furthermore, the integer does not have leading zeros, except in the case of the number '0'.

"""


def solution(numbers):
    carry = 1

    for i in range(len(numbers) -1, -1, -1):
        new_number = numbers[i] + carry
        numbers[i], carry = new_number % 10, 1 if new_number >= 10 else 0

    return numbers


if __name__ == "__main__":
    print(solution([2, 9, 9]))