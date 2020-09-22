"""
Find Duplicates

This problem was recently asked by Amazon:

Given an array of size n, and all values in the array are in the range 1 to n, find all the duplicates.

"""


def solution(nums):
    duplicated = []

    for n in nums:
        index = abs(n) - 1
        if nums[index] < 0:
            duplicated.append(abs(n))
        else:
            nums[index] = nums[index] * -1
    return duplicated


if __name__ == "__main__":
    print(solution([4,3,2,7,8,2,3,1]))
    # [2, 3]