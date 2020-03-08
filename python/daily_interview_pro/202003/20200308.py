"""
Contiguous Subarray with Maximum Sum

This problem was recently asked by Twitter:

You are given an array of integers. Find the maximum sum of all possible contiguous subarrays of the array.

Example:

[34, -50, 42, 14, -5, 86]

Given this input array, the output should be 137. The contiguous subarray with the largest sum is [42, 14, -5, 86].

Your solution should run in linear time.
"""


def brute_force(array):
    max_sum = 0

    for i in range(len(array)):
        for j in range(i, len(array) + 1):
            max_sum = max(max_sum, sum(array[i: j]))

    return max_sum


def solution(array):
    max_ending_here, max_so_far = (0, 0)

    for number in array:
        max_ending_here = max(number, max_ending_here + number)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


if __name__ == "__main__":
    array = [34, -50, 42, 14, -5, 86]

    print(f"Brute force({array})", brute_force(array))
    print(f"Solution({array})", solution(array))