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


def solution(node, value):
    to_visit = [(node, 1)]

    by_level = {}

    target_level = None
    while to_visit:
        current, level = to_visit.pop()

        if current.value == value:
            target_level = level
        else:
            by_level.setdefault(level, [])
            by_level[level].append(current.value)

        if current.right:
            to_visit.append((current.right, level + 1))

        if current.left:
            to_visit.append((current.left, level + 1))

    return by_level[target_level]


def list_cousins(node, value):
    height, parent_value = find_node(node, value, None, 0)
    return get_cousins(node, value, parent_value, height)


def find_node(node, value, parent_value, height):
    if node is None:
        return False

    if node.value == value:
        return (height, parent_value)

    return find_node(node.left, value, node.value, height + 1) or find_node(
        node.right, value, node.value, height + 1
    )


def get_cousins(node, value, parent_value, height):
    if node is None or node.value == parent_value:
        return []

    if height == 0:
        return [node.value]

    return get_cousins(node.left, value, parent_value, height - 1) + get_cousins(
        node.right, value, parent_value, height - 1
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
    print(list_cousins(root, 5))
