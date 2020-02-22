"""
Two-Sum

This problem was recently asked by Facebook:

You are given a list of numbers, and a target number k.
Return whether or not there are two numbers in the list that add up to k.

Example:
Given [4, 7, 1 , -3, 2] and k = 5,
return true since 4 + 1 = 5.

Try to do it in a single pass of the list.
"""

import bisect


def solution(array, target):
    """Using O(N) space and O(N) complexity"""
    seen = set()

    for number in array:
        if target - number in seen:
            return True

        seen.add(number)

    return False


def space_solution(array, target):
    """Using O(1) space and O(N log N) complexity."""
    array.sort()

    for index in range(len(array)):
        look_for_target = target - array[index]

        index_found = binary_search(array, look_for_target)
        if index_found == -1:
            continue

        # We have to exclude the current index when looking for a
        # target
        if index_found != index:
            return True

        if index_found + 1 < len(array) and array[index_found + 1] == target:
            return True
        elif index_found - 1 >= 0 and array[index - 1] == target:
            return True

    return False


def binary_search(array, target):
    start, end = 0, len(array)
    index = bisect.bisect_left(array, target, start, end)

    if 0 <= index < end and array[index] == target:
        return index

    return -1


if __name__ == "__main__":
    array, target = [4, 7, 1, -3, 2], 6
    print(f"Solution({array}, {target}) ->", solution(array, target))
    print(f"Solution({array}, {target}) ->", space_solution(array, target))