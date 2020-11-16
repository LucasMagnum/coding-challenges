"""
Move Zeros

This problem was recently asked by Facebook:

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""

def solution(nums):
    k = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[k] = nums[i]
            k += 1

    for j in range(k, len(nums)):
        nums[j] = 0


if __name__ == "__main__":
    nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
    solution_2(nums)
    print(nums)
    # [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
