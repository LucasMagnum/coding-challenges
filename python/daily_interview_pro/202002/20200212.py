"""
Floor and Ceiling of a Binary Search Tree

Given an integer k and a binary search tree, find the floor (less than or equal to) of k, and the ceiling (larger than or equal to) of k. If either does not exist, then print them as None.

"""


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def solution(node, k, floor=None, ceil=None):
    if not node:
        return floor, ceil

    if node.value == k:
        return k, k

    if node.value < k:
        return solution(node.right, k, node.value, ceil)
    return solution(node.left, k, floor, node.value)


if __name__ == "__main__":
    root = Node(8)
    root.left = Node(4)
    root.right = Node(12)

    root.left.left = Node(2)
    root.left.right = Node(6)

    root.right.left = Node(10)
    root.right.right = Node(14)

    print(f"Solution({root}) -> ", solution(root, 5))
