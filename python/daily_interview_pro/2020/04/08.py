"""
Min Range Needed to Sort

This problem was recently asked by Twitter:

Given a list of integers, return the bounds of the minimum range that must be sorted so that the whole list would be sorted.

Example:
Input: [1, 7, 9, 5, 7, 8, 10]
Output: (1, 5)
Explanation:
The numbers between index 1 and 5 are out of order and need to be sorted.

"""


def solution(numbers):
    left = 0
    right = 0

    max_n = -float("inf")
    min_n = float("inf")

    for i, number in enumerate(numbers):
        max_n = max(max_n, number)
        if number < max_n:
            right = i

    for i, number in reversed(list(enumerate(numbers))):
        min_n = min(min_n, number)
        if min_n < number:
            left = i

    return (left, right)


if __name__ == "__main__":
    print(solution([1, 7, 9, 5, 7, 8, 10]))
