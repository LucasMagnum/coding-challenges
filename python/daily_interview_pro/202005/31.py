"""
Sorting Window Range

This problem was recently asked by Twitter:

Given a list of numbers, find the smallest window to sort such that the whole list will be sorted.
If the list is already sorted return (0, 0). You can assume there will be no duplicate numbers.

Example:
Input: [2, 4, 7, 5, 6, 8, 9]
Output: (2, 4)

Explanation: Sorting the window (2, 4) which is [7, 5, 6] will also means that the whole list is sorted.
"""


def min_window_to_sort(nums):
    lower_bound = upper_bound = -1
    max_num = float("-inf")

    for i in range(len(nums)):
        if max_num < nums[i]:
            max_num = nums[i]

        if nums[i] < max_num:
            upper_bound = i

    min_num = float("inf")
    for i in range(len(nums) -1, -1, -1):
        if nums[i] < min_num:
            min_num = nums[i]

        if min_num < nums[i]:
            lower_bound = i

    return (lower_bound, upper_bound)



if __name__ == "__main__":
    print(min_window_to_sort([2, 4, 7, 5, 6, 8, 9]))
    # (2, 4)
