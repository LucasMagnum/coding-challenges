"""
String Compression

This problem was recently asked by Twitter:

Given an array of characters with repeats, compress it in place.
The length after compression should be less than or equal to the original array.

Example:
Input: ['a', 'a', 'b', 'c', 'c', 'c']
Output: ['a', '2', 'b', 'c', '3']

"""


def solution(string):
    left = i = 0

    while i < len(string):
        char, length = string[i], 1

        while (i + 1) < len(string) and char == string[i + 1]:
            length, i = length + 1, i + 1

        string[left] = char

        if length > 1:
            string[left + 1] = length
            left += 1

        left, i = left + 1, i + 1
    return string[:left]


if __name__ == "__main__":
    string = ["a", "a", "b", "c", "c", "c"]
    print(solution(string))
