"""
Largest Product of 3 Elements

This problem was recently asked by Microsoft:

You are given an array of integers. Return the largest product that can be made by multiplying any 3 integers in the array.

Example:

[-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.

"""

from functools import reduce


def solution(array):
    """
        If the array was restricted to only contain positive integers, the solution would be fairly trivial. Simply sort the array, and multiply the first 3 elements. However, this approach no longer works if there are negative numbers involved. To account for negative numbers, we require a slight modification. First, it is important to recognize that if we are going to include negative n number, we need to have 2 so that they cancel each other out. This means that the largest product is either the product of the 3 largest numbers, or the largest number and the 2 smallest numbers (most negative).
    """
    array.sort()

    third_largest, second_largest, first_largest = array[-3], array[-2], array[-1]
    first_smallest, second_smallest = array[0], array[1]

    return max(
        third_largest * second_largest * first_largest,
        first_largest * first_smallest * second_smallest,
    )


if __name__ == "__main__":
    array = [-4, -4, 2, 8]
    print(f"Solution({array}) ->", solution(array))
