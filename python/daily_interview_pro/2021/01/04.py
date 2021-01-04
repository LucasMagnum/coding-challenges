"""
Reconstrunct Binary Tree from Preorder and Inorder Traversals

 This problem was recently asked by Microsoft:

You are given the preorder and inorder traversals of a binary tree in the form of arrays.
Write a function that reconstructs the tree represented by these traversals.

Example:
Preorder: [a, b, d, e, c, f, g]
Inorder: [d, b, e, a, f, c, g]

The tree that should be constructed from these traversals is:

    a
   / \
  b   c
 / \ / \
d  e f  g

"""

from collections import deque


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        q = deque()
        q.append(self)
        result = ''
        while len(q):
            n = q.popleft()
            result += n.val
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        return result


def reconstruct(preorder, inorder, cache=None):
    if not preorder and not inorder:
        return None

    if len(preorder) == len(inorder) == 1:
        return Node(preorder[0])

    if cache is None:
        cache = {
            value: idx
            for idx, value in enumerate(inorder)
        }

    root = Node(preorder[0])
    root_idx = cache[root.val]

    root.left = reconstruct(preorder[1:1 + root_idx], inorder[0:root_idx])
    root.right = reconstruct(preorder[1 + root_idx:], inorder[root_idx + 1:])
    return root


if __name__ == "__main__":
    tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                    ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
    print(tree)
    # abcdefg