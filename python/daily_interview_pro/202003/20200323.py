"""
3 Sum

This problem was recently asked by Twitter:

Given an array, nums, of n integers, find all unique triplets (three numbers, a, b, & c) in nums such that a + b + c = 0. Note that there may not be any triplets that sum to zero in nums, and that the triplets must not be duplicates.

Example:
Input: nums = [0, -1, 2, -3, 1]
Output: [0, -1, 1], [2, -3, 1]

"""


def brute_force(array):
    results = []

    for i, a in enumerate(array):
        for j, b in enumerate(array[i + 1 :], i):
            for c in array[j + 1 :]:
                if a + b + c == 0:
                    results.append([a, b, c])

    return results


def solution(array):
    results = []
    array.sort()

    length = len(array)

    # Range is length -2 because we need at least 3 numbers to continue
    for i in range(length - 2):

        # The sum of 3 positive numbers will always be > 0
        if array[i] > 0:
            break

        # If it's a duplicate we do not check
        if i > 0 and array[i] == array[i - 1]:
            continue

        l, r = i + 1, length - 1
        while l < r:
            total = array[i] + array[l] + array[r]

            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                results.append([array[i], array[l], array[r]])

                while l < r and array[l] == array[l + 1]:
                    l += 1

                while l < r and array[r] == array[r - 1]:
                    r -= 1

                l += 1
                r -= 1

    return results


if __name__ == "__main__":
    array = [0, -1, 2, -3, 1]
    print(brute_force(array))
    print(solution(array))
