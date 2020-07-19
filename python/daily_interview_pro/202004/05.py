"""
Arithmetic Binary Tree

 This problem was recently asked by Apple:

You are given a binary tree representation of an arithmetic expression. In this tree, each leaf is an integer value,, and a non-leaf node is one of the four operations: '+', '-', '*', or '/'.

Write a function that takes this tree and evaluates the expression.

Example:

    *
   / \
  +    +
 / \  / \
3  2  4  5

This is a representation of the expression (3 + 2) * (4 + 5), and should return 45.


"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

OPERATORS = {
    PLUS: lambda x, y: x + y,
    MINUS: lambda x, y: x - y,
    TIMES: lambda x, y: x * y,
    DIVIDE: lambda x, y: x / y,
}


def solution(tree):
    if tree.val not in OPERATORS:
        return tree.val

    operation = OPERATORS[tree.val]
    return operation(solution(tree.left), solution(tree.right))


if __name__ == "__main__":
    tree = Node(TIMES)
    tree.left = Node(PLUS)
    tree.left.left = Node(3)
    tree.left.right = Node(2)
    tree.right = Node(PLUS)
    tree.right.left = Node(4)
    tree.right.right = Node(5)
    print(solution(tree))
