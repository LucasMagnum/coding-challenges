"""
Level of tree with Maximum Sum

This problem was recently asked by Microsoft:

Given a binary tree, find the level in the tree where the sum of
all nodes on that level is the greatest.

Here's an example and some starter code.

    1          Level 0 - Sum: 1
   / \
  4   5        Level 1 - Sum: 9
 / \ / \
3  2 4 -1      Level 2 - Sum: 8

"""

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    return f"(Value: {self.value} Left: {self.left} Right: {self.right})"


def tree_level_max_sum(root):
    stack = [(root, 0)]
    totals = {}

    while stack:
        node, level = stack.pop()
        totals[level] = totals.get(level, 0) + node.value

        if node.left:
            stack.append((node.left, level + 1))
        if node.right:
            stack.append((node.right, level + 1))

    max_level, _ = max(totals.items(), key=lambda args: args[1])
    return max_level


if __name__ == "__main__":

    n3 = Node(4, Node(3), Node(2))
    n2 = Node(5, Node(4), Node(-1))
    n1 = Node(1, n2, n3)

    print(tree_level_max_sum(n1))
    # Should print 1 as level 1 has the highest level sum