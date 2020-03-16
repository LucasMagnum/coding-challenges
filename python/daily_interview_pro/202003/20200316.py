"""
Validate Binary Search Tree

This problem was recently asked by Facebook:

You are given the root of a binary search tree. Return true if it is a valid binary search tree, and false otherwise. Recall that a binary search tree has the property that all values in the left subtree are less than or equal to the root, and all values in the right subtree are greater than or equal to the root.

"""


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def is_bst(root, min_key=float("-inf"), max_key=float("inf")):
    if root is None:
        return True

    if root.key <= min_key or root.key >= max_key:
        return False

    return is_bst(root.left, min_key, root.key) and is_bst(
        root.right, root.key, max_key
    )


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    print(is_bst(root))
