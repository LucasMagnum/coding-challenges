"""
Find the Single Element in an Array of Duplicates

This problem was recently asked by Apple:

Given an array of integers, arr, where all numbers occur twice except one number which occurs once, find the number. Your solution should ideally be O(n) time and use constant extra space.
Example:
Input: arr = [7, 3, 5, 5, 4, 3, 4, 8, 8]
Output: 7

"""

def solution(nums):
    checker = 0

    for number in nums:
        checker ^= number

    return checker


if __name__ == "__main__":
    nums = [1, 4, 1, 3, 4, 5, 6, 5, 6, 3, 0]
    print(solution(nums))
    # 3