"""
ZigZag Binary Tree

This problem was recently asked by Apple:

Given a binary tree, return the list of node values in zigzag order traversal. Here's an example

# Input:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
#
# Output: [1, 3, 2, 4, 5, 6, 7]

"""


class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right


def zigzag_order(tree):
    result = []
    current_level = []
    next_level = []

    left_to_right = True
    current_level.append(tree)

    while current_level:
        node = current_level.pop()
        result.append(node.value)

        if left_to_right:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        else:
            if node.right:
                next_level.append(node.right)
            if node.left:
                next_level.append(node.left)

        if not current_level:
            left_to_right = not left_to_right
            current_level, next_level = next_level, current_level

    return result


if __name__ == "__main__":
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n2 = Node(2, n4, n5)
    n3 = Node(3, n6, n7)
    n1 = Node(1, n2, n3)

    print(zigzag_order(n1))
    # [1, 3, 2, 4, 5, 6, 7]