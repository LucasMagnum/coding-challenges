"""
Rotate Array

This problem was recently asked by Facebook:

Given an array and an integer k, rotate the array by k spaces.
Do this without generating a new array and without using extra space.

"""


def rotate_list(nums, k):
    reverse(nums, 0, k)
    reverse(nums, k, len(nums))
    reverse(nums, 0, len(nums))


def reverse(nums, start, end):
    for i in range((end - start) // 2):
        nums[start + i], nums[end - 1 - i] = nums[end - 1 - i], nums[start + i]



if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    rotate_list(a, 2)
    print(a)
    # [3, 4, 5, 1, 2]
