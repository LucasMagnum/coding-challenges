"""
Validate Binary Search Tree

This problem was recently asked by Facebook:

You are given the root of a binary search tree.
Return true if it is a valid binary search tree, and false otherwise.
Recall that a binary search tree has the property that all values
in the left subtree are less than or equal to the root,
and all values in the right subtree are greater than or
equal to the root.

"""

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def is_bst(root):
    def validate(root, min_value, max_value):
        if root is None:
            return True

        if root.key <= min_value or root.key >= max_value:
            return False

        return (validate(root.left, min_value, root.key) and
                validate(root.right, root.key, max_value))

    return validate(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    a = TreeNode(5)
    a.left = TreeNode(3)
    a.right = TreeNode(7)
    a.left.left = TreeNode(1)
    a.left.right = TreeNode(4)
    a.right.left = TreeNode(6)
    print(is_bst(a))

    #    5
    #   / \
    #  3   7
    # / \ /
    #1  4 6