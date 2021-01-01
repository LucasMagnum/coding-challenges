"""
This problem was recently asked by Apple:

A fixed point in a list is where the value is equal to its index.
So for example the list [-5, 1, 3, 4], 1 is a fixed point in the list
since the index and value is the same.

Find a fixed point (there can be many, just return 1) in a sorted list of distinct elements,
or return None if it doesn't exist.

"""


def find_fixed_point(nums):

    def binary_search(nums, low, high):
        if low == high:
            return None

        mid = (low + high) // 2

        if nums[mid] == mid:
            return mid

        if nums[mid] < mid:
            return binary_search(nums, mid + 1, high)
        return binary_search(nums, low, mid)

    return binary_search(nums, 0, len(nums) - 1)





if __name__ == "__main__":
    print(find_fixed_point([-5, 1, 3, 4]))
    # 1