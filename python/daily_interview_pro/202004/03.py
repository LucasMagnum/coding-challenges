"""
Longest Increasing Subsequence

This problem was recently asked by Microsoft:

You are given an array of integers. Return the length of the longest increasing subsequence (not necessarily contiguous) in the array.

Example:
[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

The following input should return 6 since the longest increasing subsequence is 0, 2, 6, 9 , 11, 15.

"""


def solution(array):
    if not array:
        return 0

    cache = [1] * len(array)

    for i in range(1, len(array)):
        for j in range(i):
            if array[i] > array[j]:
                cache[i] = max(cache[i], cache[j] + 1)
            
    return max(cache)



if __name__ == "__main__":
    print(solution([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))