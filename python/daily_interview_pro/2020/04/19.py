"""
This problem was recently asked by Apple:

Given an array of integers, arr, where all numbers occur twice except one number which occurs once, find the number.
Your solution should ideally be O(n) time and use constant extra space.

Example:
Input: arr = [7, 3, 5, 5, 4, 3, 4, 8, 8]
Output: 7

"""


def solution(array):
    checker = 0

    for item in array:
        checker ^= item

    return checker


if __name__ == "__main__":
    print(solution([7, 3, 5, 5, 4, 3, 4, 8, 8]))
