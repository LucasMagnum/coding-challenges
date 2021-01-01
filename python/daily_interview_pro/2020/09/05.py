"""
Array to Binary Search Tree

This problem was recently asked by Apple:

Given a sorted array, convert it into a binary search tree.

Can you do this both recursively and iteratively?

"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

    def __str__(self):
        return f"{self.val}, ({self.left}, {self.right})"


def solution_recursive(array, start=0, end=None):
    if end is None:
        end = len(array)

    if start >= end:
        return

    mid = (start + end) // 2

    node = Node(array[mid])
    node.left = solution_recursive(array, start, mid)
    node.right = solution_recursive(array, mid + 1, end)

    return node

def solution_iterative(array):
    stack = []
    node = Node(0)

    if not array:
        return

    stack.append([array, node])
    while stack:
        items, parent_node = stack.pop()

        if not items:
            continue

        if len(items) == 1:
            mid = 0
        else:
            mid = len(items) // 2

        parent_node.val = items[mid]
        if mid != 0:
            parent_node.left = Node(0)
            stack.append([items[0:mid], parent_node.left])

        if mid + 1 != len(items):
            parent_node.right = Node(0)
            stack.append([items[mid + 1:], parent_node.right])

    return node


if __name__ == "__main__":
    print(solution_recursive([-10, -3, 0, 5, 9]))
    print(solution_iterative([-10, -3, 0, 5, 9]))