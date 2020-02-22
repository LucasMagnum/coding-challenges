"""
First and Last Indices of an Element in a Sorted Array

This problem was recently asked by AirBNB:

Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.


Example:
    Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
    Output: [6,8]

    Input: A = [100, 150, 150, 153], target = 150
    Output: [1,2]

    Input: A = [1,2,3,4,5,6,10], target = 9
    Output: [-1, -1]
"""
from typing import List


def brute_force(array: List[int], target: int) -> List[int]:
    """Two pointers approach, check list in both sides and
    stop when find the target."""
    start, end = 0, len(array) - 1

    while start < end:

        if array[start] == target and array[end] == target:
            return start, end

        if array[start] != target:
            start += 1

        if array[end] != target:
            end -= 1

    return -1, -1


def binary_search_solution(array, target):
    def binary_search(start, end, lowest=True):
        if end < start:
            return -1

        middle = start + (end - start) // 2

        if lowest:
            if (middle == 0 or target > array[middle - 1]) and array[middle] == target:
                return middle

            # If target is bigger than the middle we should look into the right side
            # When it's the lowest we should keep going left while it's the first one
            elif target > array[middle]:
                return binary_search(middle + 1, end, lowest)
            return binary_search(start, middle - 1, lowest)
        else:
            if (middle == len(array) - 1 or target < array[middle + 1]) and array[
                middle
            ] == target:
                return middle

            # If target is smaller than the middle we should look into the left side
            # When it's latest we should keep going right while it's the last one
            elif target < array[middle]:
                return binary_search(start, middle - 1, lowest)
            return binary_search(middle + 1, end, lowest)

    first = binary_search(0, len(array) - 1, True)
    last = binary_search(0, len(array) - 1, False)

    return (first, last)


if __name__ == "__main__":
    array, target = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15], 9
    print(f"Solution({array}, {target})", brute_force(array, target))

    array, target = [100, 150, 150, 153], 150
    print(f"Solution({array}, {target})", brute_force(array, target))

    array, target = [1, 2, 3, 4, 5, 6, 10], 9
    print(f"Solution({array}, {target})", brute_force(array, target))

    array, target = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15], 9
    print(f"Solution({array}, {target})", binary_search_solution(array, target))
