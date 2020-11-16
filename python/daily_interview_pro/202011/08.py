"""
Count Number of Unival Subtrees

This problem was recently asked by Microsoft:

A unival tree is a tree where all the nodes have the same value. Given a binary tree, return the number of unival subtrees in the tree.

For example, the following tree should return 5:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

The 5 trees are:
- The three single '1' leaf nodes. (+3)
- The single '0' leaf node. (+1)
- The [1, 1, 1] tree at the bottom. (+1)
"""

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def count_unival_subtrees(root):
    def count(node):
        if not node:
            return 0, True

        left, is_left_unival = count(node.left)
        right, is_right_unival = count(node.right)

        total = left + right

        if is_left_unival and is_right_unival:
            if node.left and node.val != node.left.val:
                return total, False

            if node.right and node.val != node.right.val:
                return total, False

            return total + 1, True
        return total, False

    return count(root)[0]


if __name__ == "__main__":
    a = Node(0)
    a.left = Node(1)
    a.right = Node(0)
    a.right.left = Node(0)
    a.right.right = Node(0)
    a.right.left.left = Node(1)
    a.right.left.right = Node(1)

    print(count_unival_subtrees(a))
    # 5