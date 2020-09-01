"""
Clone Trees

This problem was recently asked by Facebook:

Given two binary trees that are duplicates of one another, and given a node in one tree,
find that correponding node in the second tree.

For instance, in the tree below, we're looking for Node #4.

For this problem, you can assume that:
- There can be duplicate values in the tree (so comparing node1.value == node2.value isn't going to work).

Can you solve this both recursively and iteratively?
"""


class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def solution_recursive(a, b, node):
    if a == node:
        return b

    if a.left and b.left:
        found = solution_recursive(a.left, b.left, node)
        if found:
            return found

    if a.right and b.right:
        found = solution_recursive(a.right, b.right, node)
        if found:
            return found

    return None


def solution(a, b, node):
    stack = [(a, b)]

    while len(stack):
        (a,b) = stack.pop()

        if a == node:
            return b

        if a.left and b.left:
            stack.append((a.left, b.left))

        if b.right and b.right:
            stack.append((a.right, b.right))

    return None


if __name__ == "__main__":
    #  1
    # / \
    #2   3
    #   / \
    #  4*  5
    a = Node(1)
    a.left = Node(2)
    a.right = Node(3)
    a.right.left = Node(4)
    a.right.right = Node(5)

    b = Node(1)
    b.left = Node(2)
    b.right = Node(3)
    b.right.left = Node(4)
    b.right.right = Node(5)

    print(solution_recursive(a, b, a.right.left))
    print(solution(a, b, a.right.left))
    # 4