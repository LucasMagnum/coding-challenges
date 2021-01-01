"""
Leaf-Similar Trees

This problem was recently asked by Microsoft:

Given a tree, the leaves form a certain order from left to right. Two trees are considered "leaf-similar" if their leaf orderings are the same.

For instance, the following two trees are considered leaf-similar because their leaves are [2, 1]:

    3
   / \
  5   1
   \
    2
    7
   / \
  2   1
   \
    2

"""


class Node(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


def solution(root1, root2):
    if root1 and root2:
        return dfs(root1) == dfs(root2)

    return False


def dfs(root):
    if root is None:
        return []

    if not root.left and not root.right:
        return [root.val]

    return dfs(root.left) + dfs(root.right)


if __name__ == "__main__":
    #    3
    #   / \
    #  5   1
    # / \
    #6   2

    t1 = Node(3)
    t1.left = Node(5)
    t1.right = Node(1)
    t1.left.left = Node(6)
    t1.left.right = Node(2)

    #    7
    #   / \
    #  2   1
    # /  \
    # 6   2
    t2 = Node(7)
    t2.left = Node(2)
    t2.right = Node(1)
    t2.left.left = Node(6)
    t2.left.right = Node(2)

    print(solution(t1, t2))
    # True