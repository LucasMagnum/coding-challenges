"""
Binary Tree Level with Minimum Sum

This problem was recently asked by Twitter:

You are given the root of a binary tree. Find the level for the binary tree with the minimum sum, and return that value.

For instance, in the example below, the sums of the trees are 10, 2 + 8 = 10, and 4 + 1 + 2 = 7. So, the answer here should be 7.

"""

from collections import defaultdict


class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def minimum_level_sum(root):
    to_visit = [(root, 0)]

    level_to_sum = defaultdict(int)

    while to_visit:
        node, level = to_visit.pop()
        level_to_sum[level] += node.val

        if node.right:
            to_visit.append((node.right, level + 1))

        if node.left:
            to_visit.append((node.left, level + 1))

    level = min(level_to_sum, key=level_to_sum.get)
    return level_to_sum[level]


if __name__ == "__main__":
    #     10
    #    /  \
    #   2    8
    #  / \    \
    # 4   1    2
    node = Node(10)
    node.left = Node(2)
    node.right = Node(8)
    node.left.left = Node(4)
    node.left.right = Node(1)
    node.right.right = Node(2)

    print(minimum_level_sum(node))
