"""
Iterative In-Order Tree

This problem was recently asked by LinkedIn:

Given a binary tree, perform an in-order traversal both recursively and iteratively.

"""


class Node:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def inorder(node):
    if not node:
        return

    inorder(node.left)
    print(node.val, end=" ")
    inorder(node.right)


def inorder_iterative(node):
    stack = [(node, False)]

    while stack:
        node, explored = stack.pop()
        if not node:
            continue

        if explored:
            print(node.val, end=" ")
            continue

        stack.append((node.right, False))
        stack.append((node, True))
        stack.append((node.left, False))


if __name__ == "__main__":
    #     12
    #    /  \
    #   6    4
    #  / \   / \
    # 2   3 7   8
    n = Node(12, Node(6, Node(2), Node(3)), Node(4, Node(7), Node(8)))

    print("Inorder recursive")
    inorder(n)
    # 2 6 3 12 7 4 8

    print()
    print("Inorder iterative")
    inorder_iterative(n)
    # 2 6 3 12 7 4 8