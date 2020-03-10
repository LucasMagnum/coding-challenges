"""
First Common Ancestor

Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree.

Avoid storing additional nodes in a data structure.

Note: This is not necessarily a binary search tree.

"""

from data import TreeNode, build_tree


def using_parent_link(tree, first, second):
    """ Go up while the parents match """
    delta = depth(first) - depth(second)

    shallower = second if delta > 0 else first
    deeper = first if delta > 0 else second

    deeper = go_up_by(deeper, abs(delta))

    while shallower != deeper and shallower and deeper:
        shallower = shallower.parent
        deeper = deeper.parent

    return None if shallower is None or deeper is None else shallower


def go_up_by(node: TreeNode, delta: int) -> TreeNode:
    while delta and node:
        node = node.parent
        delta -= 1

    return node


def depth(node: TreeNode) -> int:
    depth = 0

    while node:
        node = node.parent
        depth += 1

    return depth


if __name__ == "__main__":
    array = [3, 6, 7, 8, 12, 14, 16]
    tree = build_tree(array, 0, len(array) - 1)
    first = tree.left.left  # 3
    second = tree.right.right  # 16

    print(using_parent_link(tree, first, second))
