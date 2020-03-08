"""
Move Zeros

This problem was recently asked by Facebook:

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""


def solution(array):
    position = 0

    for i in range(len(array)):
        if array[i] != 0:
            array[position] = array[i]
            position += 1

    for index in range(position, len(array)):
        array[index] = 0

    return array


if __name__ == "__main__":
    array = [1, 1, 0, 3, 12, 5, 0, 0, 7, 0, 9, 15, 0, 0, 4, 0]
    print(f"Solution({array}) ->", solution(array))
