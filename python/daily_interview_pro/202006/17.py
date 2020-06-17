"""
Partition a List

This problem was recently asked by LinkedIn:

Given a list of numbers and an integer k, partition/sort the list such that the all numbers
less than k occur before k, and all numbers greater than k occur after the number k.

"""


def solution(array, k):
    smaller_idx = 0
    equal_idx = 0
    larger_idx = len(array) - 1

    while equal_idx <= larger_idx:
        item = array[equal_idx]

        if item < k:
            array[smaller_idx], array[equal_idx] = array[equal_idx], array[smaller_idx]
            smaller_idx += 1
            equal_idx += 1

        if item == k:
            equal_idx += 1

        if item > k:
            array[larger_idx], array[equal_idx] = array[equal_idx], array[larger_idx]
            larger_idx -= 1

    return array



if __name__ == "__main__":
    print(solution([2, 2, 2, 5, 2, 2, 2, 2, 5], 3))