"""
Random Node

You are implementing a binary search tree class from scratch which,
in addition to insert, find, and delete, has a method get_random_node
which returns a random node from the tree.

All nodes should be equally likely to be chosen. Design and implement
an algorithm for get_random_node, and explain how you would implement the rest of
the methods.

"""

import random
from data import build_tree


class Tree:
    def __init__(self, root=None):
        self.root = root
        self.size = self.root.size if self.root else 0

    def get_random_node(self):
        if self.root is None:
            return

        ith = random.randint(0, self.size)
        return self.root.get_ith_node(ith)


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.size = 1

    def __str__(self):
        return f"{self.value}"

    def insert_in_order(self, value):
        if value <= self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert_in_order(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert_in_order(value)

        self.size += 1

    def find(self, value):
        if self.value == value:
            return self

        if value <= self.value:
            return self.left.find(value) if self.left else None
        return self.right.find(value) if self.right else None

    def get_ith_node(self, ith):
        left_size = 0 if self.left is None else self.left.size

        if ith < left_size:
            return self.left.get_ith_node(ith)

        elif ith == left_size:
            return self.value

        else:
            # Skipping over left size + 1 nodes, so subtract them
            return self.right.get_ith_node(ith - left_size + 1)


def brute_force(root):
    nodes = []

    to_visit = [root]
    while to_visit:
        root = to_visit.pop()

        if not root:
            continue

        nodes.append(root)
        to_visit.append(root.left)
        to_visit.append(root.right)

    random_index = random.randint(0, len(nodes))
    return nodes[random_index]


if __name__ == "__main__":
    root = build_tree(range(0, 100), 0, 99)

    tree = TreeNode(root.value)
    to_visit = [root]
    while to_visit:

        node = to_visit.pop()

        if node.left:
            tree.insert_in_order(node.left.value)
            to_visit.append(node.left)

        if node.right:
            tree.insert_in_order(node.right.value)
            to_visit.append(node.right)

    print(brute_force(root))
    print(Tree(tree).get_random_node())
