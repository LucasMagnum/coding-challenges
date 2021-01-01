"""
Number of Cousins

This problem was recently asked by Amazon:

Given a binary tree and a given node value, return all of the node's cousins.
Two nodes are considered cousins if they are on the same level of the tree with different parents.
You can assume that all nodes will have their own unique value.
"""

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def solution(tree, val):
    node_data = find_node(tree, val, None, 0)

    if not node_data:
        return []

    height, parent_value = node_data
    # Node found is root and root has no cousins
    if not parent_value:
        return []

    return find_cousins(tree, height, parent_value)


def find_cousins(tree, height, parent_value):
    if not tree or tree.value == parent_value:
        return []

    if height == 0:
        return [tree.value]

    return (
        find_cousins(tree.left, height - 1, parent_value) +
        find_cousins(tree.right, height - 1, parent_value)
    )


def find_node(tree, val, parent_value, height):
    if tree is None:
        return

    if tree.value == val:
        return (height, parent_value)

    return (
        find_node(tree.left, val, tree.value, height + 1) or
        find_node(tree.right, val, tree.value, height + 1)
    )


if __name__ == "__main__":
    #     1
    #    / \
    #   2   3
    #  / \   \
    # 4   6   5
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right = Node(3)
    root.right.right = Node(5)

    print(solution(root, 5))
    # [4, 6]