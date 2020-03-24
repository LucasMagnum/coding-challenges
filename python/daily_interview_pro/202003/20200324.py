"""
Largest BST in a Binary Tree

This problem was recently asked by Twitter:

You are given the root of a binary tree. Find and return the largest subtree of that tree, which is a valid binary search tree.

"""
from collections import namedtuple

result = namedtuple("Result", "size, min, max")


def largest_bst_subtree(root):
    max_size = 0
    max_root = None

    def helper(root):
        nonlocal max_size, max_root

        if root is None:
            return result(0, float("inf"), float("-inf"))

        left = helper(root.left)
        right = helper(root.right)

        if root.key > left.max and root.key < right.min:
            size = left.size + right.size + 1
            if size > max_size:
                max_size = size
                max_root = root

            return result(size, min(root.key, left.min), max(root.key, right.max))
        return result(0, float("-inf"), float("inf"))

    helper(root)
    return max_root


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def __str__(self):
        # preorder traversal
        answer = str(self.key)
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)
        return answer


if __name__ == "__main__":
    node = TreeNode(5)
    node.left = TreeNode(6)
    node.right = TreeNode(7)
    node.left.left = TreeNode(2)
    node.right.left = TreeNode(4)
    node.right.right = TreeNode(9)
    print(largest_bst_subtree(node))
