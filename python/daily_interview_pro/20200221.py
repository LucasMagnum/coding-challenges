"""
Minimum Size Subarray Sum

This problem was recently asked by Amazon:

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:
    Input: s = 7, nums = [2,3,1,2,4,3]
    Output: 2

Explanation: the subarray [4,3] has the minimal length under the problem constraint.

"""


def brute_force(array, target):
    minimum_value = (float("inf"), None)

    for i in range(len(array)):
        for j in range(len(array)):
            array_slice = array[i: j + 1]

            if sum(array_slice) < target:
                continue

            if len(array_slice) < minimum_value[0]:
                minimum_value = (len(array_slice), array_slice)

    return (0, None) if minimum_value[0] == float("inf") else minimum_value


def solution(array, target):
    left, right = 0, -1

    total = 0
    result = len(array) + 1

    while (left < len(array)):
        if total < target and right + 1 < len(array):
            # if total is smaller, keep moving right index to increase window
            right += 1
            total += array[right]

        else:
            # if total >= target, move left to shrink window
            total -= array[left]
            left += 1

        if total >= target:
            result = min(result, right - left + 1)

    if result == len(array) + 1:
        return 0

    return result


if __name__ == "__main__":
    array, target = [1, 4, 6, 7, 3, 2, 1, 5, 9], 20
    print(f"Brute force({array})", brute_force(array, target))
    print(f"Solution({array})", solution(array, target))