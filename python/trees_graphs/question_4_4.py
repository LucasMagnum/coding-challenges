"""
Check balanced
    Implement a function to check if a binary tree is balanced. For the purposes of
    this question, a balanced tree is defined to be a tree such that the heights of the two subtrees
    of any node never differ by more than one.
"""
import random
from typing import List


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = left

    def __str__(self):
        return f"{self.value}"


def check_balanced(tree):
    return check_height(tree) > 0


def check_height(node):
    if not node:
        return -1

    sentinel_value = float("-inf")

    left_height = check_height(node.left)
    if left_height == sentinel_value:
        return sentinel_value

    right_height = check_height(node.right)
    if right_height == sentinel_value:
        return sentinel_value

    if abs(left_height - right_height) > 1:
        return sentinel_value

    return max(left_height, right_height) + 1


def build_tree(array, start, end, unbalanced=True):
    if end < start:
        return

    mid = (start + end) // 2

    node = TreeNode(array[mid])
    node.left = build_tree(array, start, mid - 1, unbalanced)

    if random.randint(0, 10) > 5 or not unbalanced:
        node.right = build_tree(array, mid + 1, end, unbalanced)

    return node


if __name__ == "__main__":
    tree_unbalanced = build_tree(list(range(1, 101)), 0, 99)
    tree_balanced = build_tree(list(range(1, 101)), 0, 99, unbalanced=False)
    print("Is balanced (unbalanced) ->", check_balanced(tree_unbalanced))
    print("Is balanced (balanced) ->", check_balanced(tree_balanced))
