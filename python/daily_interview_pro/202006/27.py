"""
Find subtree

This problem was recently asked by Apple:

Given 2 binary trees t and s, find if s has an equal subtree in t,
where the structure and the values are the same.

Return True if it exists, otherwise return False.

"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"(Value: {self.value} Left: {self.left} Right: {self.right})"


def find_subtree(subtree, tree):
    return preorder_traversal(subtree) in preorder_traversal(tree)


def preorder_traversal(node):
    if node is None:
        return ''
    return str(node.value) + '-' + preorder_traversal(node.left) + '-' + preorder_traversal(node.right)



if __name__ == "__main__":
    t3 = Node(4, Node(3), Node(2))
    t2 = Node(5, Node(4), Node(-1))
    tree = Node(1, t2, t3)

    subtree = Node(4, Node(3), Node(2))
    """
    Tree t:
          1
         / \
        4   5
       / \ / \
      3  2 4 -1

    Tree s:
      4
     / \
    3   2
    """

    print(find_subtree(subtree, tree))
    # True
