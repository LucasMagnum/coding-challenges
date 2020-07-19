"""
Jump to the End

This problem was recently asked by Facebook:

Starting at index 0, for an element n at index i, you are allowed to jump at most n indexes ahead.
Given a list of numbers, find the minimum number of jumps to reach the end of the list.

Example:
Input: [3, 2, 5, 1, 1, 9, 3, 4]
Output: 2
Explanation:

The minimum number of jumps to get to the end of the list is 2:
3 -> 5 -> 4

"""


def solution(array):
    jumps = [float("inf")] * len(array)
    jumps[0] = 0

    for i, n in enumerate(array):
        for j in range(1, n + 1):
            if i + j < len(array):
                jumps[i + j] = min(jumps[i + j], jumps[i] + 1)
            else:
                break

    return jumps[-1]


if __name__ == "__main__":
    print(solution([3, 2, 5, 1, 1, 9, 3, 4]))
