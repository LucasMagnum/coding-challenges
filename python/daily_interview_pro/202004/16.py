"""
Symmetric k-ary Tree

This problem was recently asked by Microsoft:

A k-ary tree is a tree with k-children, and a tree is symmetrical
if the data of the left side of the tree is the same as the right side of the tree.

Here's an example of a symmetrical k-ary tree.
        4
     /     \
    3        3
  / | \    / | \
9   4  1  1  4  9

Given a k-ary tree, figure out if the tree is symmetrical.
"""

class Node():
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children


def is_symmetric(root):
    children_count = len(root.children)

    for i in range(children_count // 2):
        if not is_symmetric_helper(root.children[i], root.children[children_count - i - 1]):
            return False
    
    return True


def is_symmetric_helper(left, right):
    if left.value != right.value:
        return False
    
    if len(left.children) != len(right.children):
        return False
    
    children_count = len(left.children)
    for i in range(children_count):
        if not is_symmetric_helper(left.children[i], right.children[children_count - i - 1]):
            return False

    return True


if __name__ == "__main__":
    tree = Node(4)
    tree.children = [Node(3), Node(3)]
    tree.children[0].children = [Node(9), Node(4), Node(1)]
    tree.children[1].children = [Node(1), Node(4), Node(9)]
    print(is_symmetric(tree))


