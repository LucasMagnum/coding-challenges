"""

Deepest Node in a Binary Tree

his problem was recently asked by Google:

You are given the root of a binary tree. Return the deepest node (the furthest node from the root).

Example:

    a
   / \
  b   c
 /
d

The deepest node in this tree is d at depth 3.


"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        # string representation
        return self.val


def deepest(node, depth=1, max_depth=float("-inf")):
    if not node:
        return 0

    max_depth = float("-inf")

    def dfs(node, depth=1):
        if not node:
            return

        nonlocal max_depth

        max_depth = max(depth, max_depth)
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(node)
    return max_depth


if __name__ == "__main__":
    root = Node("a")
    root.left = Node("b")
    root.left.left = Node("d")
    root.right = Node("c")

    print(deepest(root))
