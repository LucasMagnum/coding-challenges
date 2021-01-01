"""
Sort a Partially Sorted List

This problem was recently asked by Uber:

You are given a list of n numbers, where every number is at most k indexes away from its properly sorted index.
Write a sorting algorithm (that will be given the number k) for this list that can solve this in O(n log k)

Example:
Input: [3, 2, 6, 5, 4], k=2
Output: [2, 3, 4, 5, 6]
As seen above, every number is at most 2 indexes away from its proper sorted index.

"""

import heapq


def solution(array, k):
    heap = []
    ordered_array = []

    k += 1

    for number in array[:k]:
        heapq.heappush(heap, number)

    for number in array[k:]:
        ordered_array.append(heapq.heapreplace(heap, number))

    while len(heap) > 0:
        ordered_array.append(heapq.heappop(heap))

    return ordered_array


if __name__ == "__main__":
    array, k = [3, 2, 6, 5, 4], 2
    print(solution(array, k))
