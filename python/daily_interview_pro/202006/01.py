"""
Determine Height Balanced Binary Tree

This problem was recently asked by Twitter:

Given a tree, find if the binary tree is height balanced or not.
A height balanced binary tree is a tree where every node's 2 subtree
do not differ in height by more than 1.

"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_height_balanced(node):
    return check_balanced(node) != -1


def check_balanced(node):
    if node is None:
        return 0

    left_height = check_balanced(node.left)
    if left_height == -1: return -1

    right_height = check_balanced(node.right)
    if right_height == -1: return -1

    if abs(check_balanced(node.left) - check_balanced(node.right)) > 1:
        return -1

    return max(right_height, left_height) + 1


if __name__ == "__main__":

    #     1
    #    / \
    #   2   3
    #  /
    # 4
    n4 = Node(4)
    n3 = Node(3)
    n2 = Node(2, n4)
    n1 = Node(1, n2, n3)

    print(is_height_balanced(n1))
    # True


    #     1
    #    /
    #   2
    #  /
    # 4
    n1 = Node(1, n2)

    print(is_height_balanced(n1))
    # False
