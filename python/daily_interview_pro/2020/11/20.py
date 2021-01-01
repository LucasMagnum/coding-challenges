"""
Array to Binary Search Tree

This problem was recently asked by Apple:

Given a sorted array, convert it into a binary search tree.

Can you do this both recursively and iteratively?

"""

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
      return f"{self.val}, ({self.left}, {self.right})"


def solution(nums, start=None, end=None):
    if not nums:
        return

    if start is None and end is None:
        start, end = 0, len(nums)

    if start >= end:
        return

    mid = (start + end) // 2

    node = Node(nums[mid])
    node.left = solution(nums, start, mid)
    node.right = solution(nums, mid + 1, end)

    return node


if __name__ == "__main__":
    n = solution([-10, -3, 0, 5, 9])
    print(n)
    # 0, (-3, (-10, (None, None), None), 9, (5, (None, None), None))