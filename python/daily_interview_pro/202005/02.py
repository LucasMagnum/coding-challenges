"""
Lowest Common Ancestor of 2 Nodes in Binary Tree

This problem was recently asked by Apple:

You are given the root of a binary tree, along with two nodes, A and B.
Find and return the lowest common ancestor of A and B.
For this problem, you can assume that each node also has a pointer to its parent,
along with its left and right child.

"""

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.val = val


def solution(root, a, b):
    """
    A simple solution to this problem would be to iterate from A to the root, and store each node in a hash set.
    Then, iterate from B to the root, and during each iteration, check if the current node is in the hash set.
    The first node you encounter that is in the hash set must be the lowest common ancestor.
    This solution has both a time and space complexity of O(N) in the worst case.

    We can optimize the space complexity of this solution by recognizing that this problem is essentially
    finding the intersection of two singly linked lists. To do this, we simply traverse from A to root, and count
    the length of the path. Similarly, we traverse from B to root, and count the length of the path.
    Next, we set our pointers at A and B, and move the pointer of the longer path forward by the difference
    in length of the two paths. Now, both pointers are the same distance from the root.
    We simply move both pointers up towards the root simultaneously until they are both at the same node. This node is the lowest common ancestor.
    """

    def depth(node):
        count = 0
        while node:
            count += 1
            node = node.parent
        return count

    depth_a, depth_b = depth(a), depth(b)
    if depth_a < depth_b:
        while depth_a < depth_b:
            b = b.parent
            depth_b -= 1

    elif depth_a > depth_b:
        while depth_a > depth_b:
            a = a.parent
            depth_a -= 1

    while a and b and (a is not b):
        a = a.parent
        b = b.parent

    return a if (a is b) else None


if __name__ == "__main__":
    #   a
    #  / \
    # b   c
    #    / \
    #   d*  e*
    root = TreeNode('a')
    root.left = TreeNode('b')
    root.left.parent = root
    root.right = TreeNode('c')
    root.right.parent = root
    a = root.right.left = TreeNode('d')
    root.right.left.parent = root.right
    b = root.right.right = TreeNode('e')
    root.right.right.parent = root.right

    print(solution(root, a, b).val)