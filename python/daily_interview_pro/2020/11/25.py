"""
Find the k-th Largest Element in a List

This problem was recently asked by Facebook:

Given a list, find the k-th largest element in the list.
Input: list = [3, 5, 2, 4, 6, 8], k = 3
Output: 5
"""

import heapq
import random


def findKthLargest(nums, k):
    heapq.heapify(nums)
    for i in range(k):
        heapq.heappop(nums)
    return heapq.heappop(nums)


def solution(nums, k):
    def select(lst, l, r, index):
        if r == l:
            return lst[l]

        pivot_idx = random.randint(l, r)
        # move pivot to beginning of the list
        lst[l], lst[pivot_idx] = lst[pivot_idx], lst[l]

        # Partition
        i = l
        for j in range(l + 1, r + 1):
            if lst[j] < lst[l]:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]

        # Move pivot to correct location
        lst[i], lst[l] = lst[l], lst[i]

        # Recursively partition one side only
        if index == i:
            return lst[i]
        elif index < i:
            return select(lst, l, i - 1, index)
        return select(lst, i + 1, r, index)

    return select(nums, 0, len(nums) - 1, k)


if __name__ == "__main__":
    print(findKthLargest([3, 5, 2, 4, 6, 8], 3))
    print(solution([3, 5, 2, 4, 6, 8], 3))
    # 5