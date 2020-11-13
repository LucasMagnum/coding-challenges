"""
First Missing Positive Integer

This problem was recently asked by Facebook:

You are given an array of integers.
Return the smallest positive integer that is not present in the array.
The array may contain duplicate entries.

For example, the input [3, 4, -1, 1] should return 2 because it is the smallest positive integer that doesn't exist in the array.

Your solution should run in linear time and use constant space.

"""

def first_missing_positive(nums):
    if not nums:
        return 1

    for i, num in enumerate(nums):
        while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
            v = nums[i]
            nums[i], nums[v - 1] = nums[v - 1], nums[i]

            if nums[i] == nums[v - 1]:
                break

    for i, num in enumerate(nums, 1):
        if num != i:
            return i
    return len(num) + 1


if __name__ == "__main__":
    print(first_missing_positive([3, 4, -1, 1, 2, 10, 12]))
    # 2