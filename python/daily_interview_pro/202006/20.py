"""
Largest Path Sum from Root To Leaf

This problem was recently asked by Google:

Given a binary tree, find and return the largest path from root to leaf.

"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def largest_path_sum(tree):
    def calculate_sum(tree):
        if tree is None:
            return (0, [])

        left_sum = calculate_sum(tree.left)
        right_sum = calculate_sum(tree.right)

        if left_sum[0] > right_sum[0]:
            return (left_sum[0] + tree.value, left_sum[1] + [tree.value])
        return (right_sum[0] + tree.value, right_sum[1] + [tree.value])

    return calculate_sum(tree)[1][::-1]


if __name__ == "__main__":
    tree = Node(1)
    tree.left = Node(3)
    tree.right = Node(2)
    tree.right.left = Node(4)
    tree.left.right = Node(5)
    #    1
    #  /   \
    # 3     2
    #  \   /
    #   5 4
    print(largest_path_sum(tree))
    # [1, 3, 5]