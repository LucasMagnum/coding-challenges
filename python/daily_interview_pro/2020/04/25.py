"""
Maximum Path Sum in Binary Tree

This problem was recently asked by Facebook:

You are given the root of a binary tree. 
Find the path between 2 nodes that maximizes the sum of all the nodes in the path, 
and return the sum. The path does not necessarily need to go through the root.

 (* denotes the max path)
       *10
       /  \
     *2   *10
     / \     \
   *20  1    -25
             /  \
            3    4
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def solution(root):
    def max_sum(root):
        if root is None:
            return float("-inf"), 0

        left_max_sum, left_path = max_sum(root.left)
        right_max_sum, right_path = max_sum(root.right)

        root_max_sum = max(0, left_path) + root.val + max(0, right_path)
        max_total_sum = max(left_max_sum, root_max_sum, right_max_sum)
        root_path = max(left_path, right_path, 0) + root.val

        return max_total_sum, root_path

    return max_sum(root)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(1)
    root.right.right = Node(-25)
    root.right.right.left = Node(3)
    root.right.right.right = Node(4)
    print(solution(root))
