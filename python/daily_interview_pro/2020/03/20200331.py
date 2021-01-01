"""
Merge List Of Number Into Ranges

This problem was recently asked by Facebook:

Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.

Example:
Input: [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
Output: ['0->2', '5->5', '7->11', '15->15']
Assume that all numbers will be greater than or equal to 0, and each element can repeat.


"""


def solution(numbers):
    if not numbers:
        return []

    ranges = []
    low, high = numbers[0], numbers[0]

    for number in numbers:
        if high + 1 < number:
            ranges.append(f"{low} -> {high}")
            low = number
        high = number
    ranges.append(f"{low} -> {high}")
    return ranges


if __name__ == "__main__":
    print(solution([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
