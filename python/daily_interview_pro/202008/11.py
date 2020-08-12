"""
Range Searching in a Sorted List

This problem was recently asked by Twitter:

Given a sorted list with duplicates, and a target number n,
find the range in which the number exists (represented as a tuple (low, high), both inclusive.

If the number does not exist in the list, return (-1, -1)).
"""


def find_num(nums, target):
    low_range = helper(nums, target, True)

    if low_range == len(nums) or nums[low_range] != target:
        return (-1, -1)

    return low_range, helper(nums, target) - 1


def helper(nums, target, leftmost=False):
    low = 0
    high = len(nums)

    while low < high:
        mid = (low + high)//2

        if target < nums[mid] or (leftmost and nums[mid] == target):
            high = mid
        else:
            low = mid + 1

    return low



if __name__ == "__main__":
    print(find_num([1, 1, 3, 5, 7], 1))
    # (0, 1)

    print(find_num([1, 2, 3, 4], 5))
    # (-1, -1)