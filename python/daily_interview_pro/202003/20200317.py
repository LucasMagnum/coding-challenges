"""
Get all Values at a Certain Height in a Binary Tree

This problem was recently asked by Amazon:
Given a binary tree, return all values given a certain height h.

Ex:
         1
        / \
       2   3
      / \   \
     4   5   7

    >> solution(3)
    [4, 5, 7]

"""
from collections import deque


class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def solution_bfs(root, height):
    result = []

    to_visit = deque([(root, 1)])

    while to_visit:
        node, node_height = to_visit.popleft()

        if node_height == height:
            result.append(node.value)

        if node.left:
            to_visit.append((node.left, node_height + 1))

        if node.right:
            to_visit.append((node.right, node_height + 1))

    return result


def solution_dfs(root, height):
    if not root:
        return []

    if height == 1:
        return [root.value]

    return (
        solution_dfs(root.left, height - 1) +
        solution_dfs(root.right, height - 1)
    )


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(7)

    print(solution_bfs(root, 3))
    print(solution_dfs(root, 3))
