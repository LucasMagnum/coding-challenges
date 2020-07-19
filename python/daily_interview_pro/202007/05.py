"""
Missing Ranges

This problem was recently asked by Google:

Given a sorted list of numbers, and two integers low and high representing the lower
and upper bound of a range, return a list of (inclusive) ranges where the numbers are missing.

A range should be represented by a tuple in the format of (lower, upper).

"""


def solution(nums, low, high):
    ranges = []

    if not nums:
        ranges.append((low, high))
        return ranges

    if low < nums[0]:
        ranges.append((low, nums[0] - 1))

    for idx in range(len(nums) - 1):
        if nums[idx + 1] - nums[idx] > 1:
            ranges.append((nums[idx] + 1, nums[idx + 1] - 1))

    if nums[-1] < high:
        ranges.append((nums[-1] + 1, high))

    return ranges


if __name__ == "__main__":
    print(solution([1, 3, 5, 10], 1, 10))
