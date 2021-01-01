"""
Sort Colors

This problem was recently asked by Apple:

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library’s sort function for this problem.

Can you do this in a single pass?

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

"""


def count_sort(array):
    counter = [0, 0, 0]

    for number in array:
        counter[number] += 1

    current_number = 0
    index = 0
    while current_number < len(counter):
        for i in range(counter[current_number]):
            array[index] = current_number
            index += 1

        current_number += 1

    return array


def linear_sort(array):
    numbers = [0, 1, 2]
    current = numbers[0]

    start, end = 0, len(array) - 1
    while current <= end:
        if array[current] == 0:
            # Swap start with current
            array[start], array[current] = array[current], array[start]
            start += 1
            current += 1

        elif array[current] == 2:
            # Swap end with current
            array[current], array[end] = array[end], array[current]
            end -= 1

        else:
            current += 1

    return array


if __name__ == "__main__":
    array = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
    print(f"count_sort({array})", count_sort(array[:]))
    print(f"linear_sort({array})", linear_sort(array[:]))
