"""
First Missing Positive Integer

This problem was recently asked by Facebook:

You are given an array of integers. Return the smallest positive integer that is not present in the array. The array may contain duplicate entries.

For example, the input [3, 4, -1, 1] should return 2 because it is the smallest positive integer that doesn't exist in the array.

Your solution should run in linear time and use constant space.
"""


def solution(array):
    if not array:
        return 1
    for i, number in enumerate(array):
        while i + 1 != array[i] and 0 < array[i] <= len(array):
            v = array[i]
            array[i], array[v - 1] = array[v - 1], array[i]
            if array[i] == array[v - 1]:
                break

    for i, number in enumerate(array, 1):
        if number != i:
            return i
    return len(array) + 1


if __name__ == "__main__":
    print(solution([3, 4, 1, -1, 0, 2, 10, 15]))
