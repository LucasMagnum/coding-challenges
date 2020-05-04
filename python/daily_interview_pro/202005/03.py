"""
Binary Tree Level with Minimum Sum

This problem was recently asked by Twitter:

You are given the root of a binary tree.
Find the level for the binary tree with the minimum sum, and return that value.

For instance, in the example below, the sums of the trees are 10, 2 + 8 = 10, and 4 + 1 + 2 = 7.
So, the answer here should be 7.

"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def solution(root):
    to_visit = [(root, 1)]
    totals = {}

    while to_visit:
        current, level = to_visit.pop()

        totals[level] = totals.get(level, 0) + current.val

        if current.left:
            to_visit.append((current.left, level + 1))

        if current.right:
            to_visit.append((current.right, level + 1))

    return min(totals.values())


def dfs(root, level=0, total={}):
    if not root:
        return 0, 0

    total[level] = total.get(level, 0) + root.val
    dfs(root.left, level + 1, total)
    dfs(root.right, level + 1, total)

    return min(total.values())


if __name__ == "__main__":
    #     10
    #    /  \
    #   2    8
    #  / \    \
    # 4   1    2
    node = Node(10)
    node.left = Node(2)
    node.right = Node(8)
    node.left.left = Node(4)
    node.left.right = Node(1)
    node.right.right = Node(2)

    print(solution(node))