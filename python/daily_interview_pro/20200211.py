"""
Non-decreasing Array with Single Modification

Hi, here's your problem today. This problem was recently asked by Microsoft:

You are given an array of integers in an arbitrary order. Return whether or not it is possible to make the array non-decreasing by modifying at most 1 element to any value.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example:

[13, 4, 7] should return true, since we can modify 13 to any value 4 or less, to make it non-decreasing.

[13, 4, 1] however, should return false, since there is no way to modify just one element to make the array non-decreasing.

Can you find a solution in O(n) time?

"""
from typing import List


def solution(array: List[int]) -> bool:
    constraints_break = 0

    for index in range(1, len(array)):
        if not array[index - 1] <= array[index]:
            constraints_break += 1

    return constraints_break <= 1


if __name__ == "__main__":
    array = [13, 4, 7, 9, 10, 11, 12, 15]
    print(f"Solution({array}) -> ", solution(array))

    array = [5, 1, 3, 2, 5]
    print(f"Solution({array}) -> ", solution(array))
