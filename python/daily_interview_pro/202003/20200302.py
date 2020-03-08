"""
Find the k-th Largest Element in a List

This problem was recently asked by Facebook:

Given a list, find the k-th largest element in the list.
Input: list = [3, 5, 2, 4, 6, 8], k = 3
Output: 5

"""

import heapq


def solution(array, k):
    return heapq.nlargest(k, array)[-1]


if __name__ == "__main__":
    array = [3, 5, 2, 4, 6, 8]
    print(f"Solution({array}) ->", solution(array, 3))
