"""
Three Equal Sums

This problem was recently asked by Apple:

Given an array of numbers, determine whether it can be partitioned into 3 arrays of equal sums.

For instance,
[0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1] can be partitioned into:
[0, 2, 1], [-6, 6, -7, 9, 1], [2, 0, 1] all of which sum to 3.
"""


def solution(array):
    size = len(array)
    target = sum(array) / 3

    current = 0
    count = 0

    for item in array:
        current += item

        if current == target:
            current = 0
            count = count + 1

    return current == 0 and count == 3



if __name__ == "__main__":
    print(solution([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
    # True
    print(solution([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1, 3]))
    # False
    print(solution([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
    # True