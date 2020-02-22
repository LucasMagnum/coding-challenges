"""
Sorting a list with 3 unique numbers

This problem was recently asked by Google:

Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

Example 1:
Input: [3, 3, 2, 1, 3, 2, 1]
Output: [1, 1, 2, 2, 3, 3, 3]

"""
import random


def solution(array):
    counter = [0, 0, 0]

    for number in array:
        counter[number - 1] += 1

    return [1] * counter[0] + [2] * counter[1] + [3] * counter[2]


if __name__ == "__main__":
    array = [random.randint(1, 3) for _ in range(50)]
    print(f"Solution({array}) -> ", solution(array))