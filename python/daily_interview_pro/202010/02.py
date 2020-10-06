"""
First and Last Indices of an Element in a Sorted Array

This problem was recently asked by AirBNB:

Given a sorted array, A, with possibly duplicated elements,
find the indices of the first and last occurrences of a target element, x.
Return -1 if the target is not found.

Example:
Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]


"""


def solution(array, target):
    first, last = -1, -1

    start, end = 0, len(array)

    while end >= start:
        mid = (start + end) // 2

        if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
            first = mid
            break
        elif target > array[mid]:
            start = mid + 1
        else:
            end = mid - 1

    if first == -1:
        return (first, last)

    start, end = 0, len(array)
    while end >= start:
        mid = (start + end) // 2
        if (mid == len(array) - 1 or target < array[mid + 1]) and array[mid] == target:
            last = mid
            break
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return (first, last)


if __name__ == "__main__":
    array = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
    target = 2
    print(solution(array, target))
    # [1, 4]
