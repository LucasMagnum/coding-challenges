"""
Make the Largest Number

This problem was recently asked by Uber:

Given a number of integers, combine them so it would create the largest number.

Example:
Input:  [17, 7, 2, 45, 72]
Output:  77245217
"""

from functools import cmp_to_key


def largestNum(nums):
    str_nums = [str(n) for n in sorted(nums, key=cmp_to_key(compare_function))]
    return "".join(str_nums)


def compare_function(a, b):
    return 1 if str(a) + str(b) < str(b) + str(a) else -1


if __name__ == "__main__":
    print(largestNum([17, 7, 2, 45, 72]))
