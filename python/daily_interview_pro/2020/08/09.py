"""
This problem was recently asked by Apple:

Given a sorted list of size n, with m unique elements (thus m < n),
modify the list such that the first m unique elements in the list will be sorted,
ignoring the rest of the list.

Your solution should have a space complexity of O(1).
Instead of returning the list (since you are just modifying the original list), you should return what m is.

"""


def remove_dups(nums):
    idx = 0

    for jdx in range(1, len(nums)):
        if nums[idx] != nums[jdx]:
            idx += 1
            nums[idx] = nums[jdx]

    for jdx in range(0, len(nums) - idx - 1):
        nums.pop()
    return idx + 1


if __name__ == "__main__":
    nums = [1, 1, 2, 3, 4, 4, 4, 4, 4, 5, 5, 6, 7, 9]
    print(remove_dups(nums))
    # 8
    print(nums)
    # [1, 2, 3, 4, 5, 6, 7, 9]

    nums = [1, 1, 1, 1, 1, 1]
    print(remove_dups(nums))
    print(nums)
    # 1
    # [1]