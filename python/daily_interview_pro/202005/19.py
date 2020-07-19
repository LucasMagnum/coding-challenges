"""
Most Frequent Subtree Sum

This problem was recently asked by LinkedIn:

Given a binary tree, find the most frequent subtree sum.

Example:

   3
  / \
 1   -3

The above tree has 3 subtrees. The root node with 3, and the 2 leaf nodes, which gives us a total of 3 subtree sums. The root node has a sum of 1 (3 + 1 + -3), the left leaf node has a sum of 1, and the right leaf node has a sum of -3. Therefore the most frequent subtree sum is 1.

If there is a tie between the most frequent sum, you can return any one of them.

Here's some starter code for the problem:

"""

from collections import defaultdict


class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def most_freq_subtree_sum(root, sums=None):
    if not root:
        return 0

    if sums is None:
        sums = defaultdict(int)

    total_root = (
        most_freq_subtree_sum(root.left, sums)
        + most_freq_subtree_sum(root.right, sums)
        + root.val
    )
    sums[total_root] += 1

    current_max = float("-inf")
    most_freq_value = None

    for k, v in sums.items():
        if v > current_max:
            current_max = v
            most_freq_value = k

    return most_freq_value


if __name__ == "__main__":
    root = Node(3, Node(1), Node(-3))
    print(most_freq_subtree_sum(root))
