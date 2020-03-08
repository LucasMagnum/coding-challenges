"""
Find the non-duplicate number

This problem was recently asked by Facebook:

Given a list of numbers, where every number shows up twice except for one number, find that one number.

Example:
Input: [4, 3, 2, 4, 1, 3, 2]
Output: 1
Here's the function signature:

def singleNumber(nums):
  # Fill this in.

print singleNumber([4, 3, 2, 4, 1, 3, 2])
# 1

Challenge: Find a way to do this using O(1) memory.
"""
from typing import List


def solution(array: List[int]) -> int:
    checker = 0

    for number in array:
        checker ^= number

    return checker


if __name__ == "__main__":
    array = [4, 3, 2, 4, 1, 3, 2]
    print(f"Solution({array}) -> ", solution(array))

    array = [9, 7, 4, 3, 2, 4, 5, 1, 3, 2, 5, 7, 9, 10]
    print(f"Solution({array}) -> ", solution(array))
