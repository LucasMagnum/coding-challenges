"""
Fixed Point

This problem was recently asked by Apple:

A fixed point in a list is where the value is equal to its index.
So for example the list [-5, 1, 3, 4], 1 is a fixed point in the list since the
index and value is the same.

Find a fixed point (there can be many, just return 1) in a sorted list of distinct elements,
 or return None if it doesn't exist.

Here is a starting point:

"""


def find_fixed_point(nums):
    return helper(0, len(nums), nums)


def helper(low, high, nums):
    if low == high:
        return None

    mid = int((low + high) / 2)

    if nums[mid] == mid:
        return mid

    if nums[mid] < mid:
        return helper(mid + 1, high, nums)

    return helper(low, mid, nums)


if __name__ == "__main__":
    print(find_fixed_point([-5, 1, 3, 4]))
    # 1
