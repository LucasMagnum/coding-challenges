"""
Maximum Non Adjacent Sum

This problem was recently asked by Google:

Given a list of positive numbers,
find the largest possible set such that no elements are adjacent numbers of each other.

"""

def max_sum(nums):
    previous_sum = 0
    current_sum = 0

    for num in nums:
        max_sum = max(current_sum, previous_sum + num)
        current_sum, previous_sum = max_sum, current_sum

    return current_sum


if __name__ == "__main__":
    print(max_sum([3, 4, 1, 1]))
    # 5
    # max sum is 4 (index 1) + 1 (index 3)

    print(max_sum([2, 1, 2, 7, 3]))
    # 9
    # max sum is 2 (index 0) + 7 (index 3)