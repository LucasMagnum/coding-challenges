"""
List of Depths:

    Given a binary tree, design an algorithm which creates a linked list of all the nodes
    at each depth (e.g., if you have a tree with depth D, you'll have D linked lists.)
"""
from typing import List


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = left

    def __str__(self):
        return f"{self.value}"


def dfs_solution(tree: TreeNode, depth=0, lists=None) -> List[TreeNode]:
    if lists is None:
        lists = []

    if not tree:
        return

    if len(lists) == depth:
        lists.append([])

    current_list = lists[depth]
    current_list.append(tree)

    dfs_solution(tree.left, depth + 1, lists)
    dfs_solution(tree.right, depth + 1, lists)

    return lists


def bfs_solution(tree: TreeNode) -> List[TreeNode]:
    lists = []

    current = []
    current.append(tree)

    while len(current) > 0:
        lists.append(current)
        previous = current

        current = []

        for node in previous:
            if node.left:
                current.append(node.left)

            if node.right:
                current.append(node.right)

    return lists


def build_tree(array, start, end):
    if end < start:
        return

    mid = (start + end) // 2

    node = TreeNode(array[mid])
    node.left = build_tree(array, start, mid - 1)
    node.right = build_tree(array, mid + 1, end)

    return node


if __name__ == "__main__":
    tree = build_tree(list(range(1, 1001)), 0, 999)

    results = dfs_solution(tree)
    print("Depths => ", len(results))
    print([(index, len(depth)) for index, depth in enumerate(results)])

    results = bfs_solution(tree)
    print("Depths => ", len(results))
    print([(index, len(depth)) for index, depth in enumerate(results)])
