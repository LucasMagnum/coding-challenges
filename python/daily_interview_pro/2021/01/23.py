"""
Duplicate Subtrees

This problem was recently asked by Uber:

Given a binary tree,
find all duplicate subtrees (subtrees with the same value and same structure)
and return them as a list of list [subtree1, subtree2, ...]
where subtree1 is a duplicate of subtree2 etc.
"""
from collections import defaultdict


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left and self.right:
            return f"({self.value}, {self.left}, {self.right})"
        if self.left:
            return f"({self.value}, {self.left})"
        if self.right:
            return f"({self.value}, None, {self.right})"
        return f"({self.value})"


def dup_trees(root, result=None, seen=None):
    def find_duplicates(root):
        if not root:
            return ""

        left = find_duplicates(root.left)
        right = find_duplicates(root.right)

        key = f"({root.value},{left},{right})"
        seen[key].append(root)
        if len(seen[key]) == 2:
            result.append(seen[key])
        return key

    result = []
    seen = defaultdict(list)
    find_duplicates(root)
    return result


if __name__ == "__main__":
    n3_1 = Node(3)
    n2_1 = Node(2, n3_1)
    n3_2 = Node(3)
    n2_2 = Node(2, n3_2)
    n1 = Node(1, n2_1, n2_2)
    # Looks like
    #     1
    #    / \
    #   2   2
    #  /   /
    # 3   3

    print(dup_trees(n1))
    # [[(3), (3)], [(2, (3)), (2, (3))]]
    # There are two duplicate trees
    #
    #     2
    #    /
    #   3
    # and just the leaf
    #
    # 3