"""
String Compression

This problem was recently asked by Twitter:

Given an array of characters with repeats, compress it in place.
The length after compression should be less than or equal to the original array.

Example:
Input: ['a', 'a', 'b', 'c', 'c', 'c']
Output: ['a', '2', 'b', 'c', '3']

"""

def solution(array):
    left = i = 0
    while i < len(array):
        char, length = array[i], 1

        while (i + 1) < len(array) and char == array[i + 1]:
            length, i = length + 1, i + 1

        array[left] = char
        if length > 1:
            len_str = str(length)
            array[left + 1: left + 1 + len(len_str)] = len_str
            left += len(len_str)

        left, i = left + 1, i + 1
    return array[:left]


if __name__ == "__main__":
    print(solution(['a', 'a', 'b', 'c', 'c', 'c']))
    # ['a', '2', 'b', 'c', '3']