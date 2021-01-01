"""
Find Missing Numbers in an Array

This problem was recently asked by Twitter:

Given an array of integers of size n, where all elements are between 1 and n inclusive,
find all of the elements of [1, n] that do not appear in the array.
Some numbers may appear more than once.

Example:

Input: [4,5,2,6,8,2,1,5]
Output: [3,7]

"""


def solution(nums):
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = -abs(nums[index])
        print(nums)

    return [index for index, n in enumerate(nums, start=1) if n > 0]


if __name__ == "__main__":
    print(solution([4, 5, 2, 6, 8, 2, 1, 5]))
