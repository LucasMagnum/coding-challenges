"""
Deepest Node in a Binary Tree

This problem was recently asked by Google:

You are given the root of a binary tree.
Return the deepest node (the furthest node from the root).


"""

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        # string representation
        return self.val


def deepest(node):
    stack = [(node, 1)]

    max_level = - 1
    max_node = None

    while stack:
        current, level = stack.pop()

        if current.left:
            stack.append((current.left, level + 1))

        if current.right:
            stack.append((current.right, level + 1))

        if level > max_level:
            max_node = current
            max_level = level

    return (max_node, max_level)


if __name__ == "__main__":
    root = Node('a')
    root.left = Node('b')
    root.left.left = Node('d')
    root.right = Node('c')

    print(deepest(root))
    # (d, 3)