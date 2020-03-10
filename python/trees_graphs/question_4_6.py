"""
Sucessor

Write an algorithm to find the "next" node (i.e., in-order successor) of a given
node in a binary search tree. You may assume that each node has a link to its parent.

"""
from data import TreeNode, build_tree


def solution(node: TreeNode) -> TreeNode:
    if not node:
        return

    if node.right is not None:
        return most_left_child(node.right)

    parent_was_left = node
    parent = node.parent

    while parent and parent.left != parent_was_left:
        parent_was_left = parent
        parent = parent.parent

    return parent


def most_left_child(node: TreeNode) -> TreeNode:
    if not node:
        return node

    while node.left:
        node = node.left

    return node


if __name__ == "__main__":
    array = [3, 6, 7, 8, 12, 14, 16]
    tree = build_tree(array, 0, len(array) - 1)

    print(f"Solution({tree})", solution(tree))
