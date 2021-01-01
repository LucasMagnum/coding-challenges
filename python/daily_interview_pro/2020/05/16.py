"""
Print a tree level-by-level, with line-breaks

This problem was recently asked by Apple:

You are given a tree, and your job is to print it level-by-level with linebreaks.

    a
   / \
  b   c
 / \ / \
d  e f  g

The output should be
a
bc
defg

"""


from collections import deque


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        to_visit = deque()
        to_visit.append((self, 0))

        result = []
        next_level = 1

        while to_visit:
            current_node, current_level = to_visit.popleft()

            # Add newline when making the transition to the next level
            if current_level == next_level:
                result.append("\n")
                next_level += 1

            if current_node.left:
                to_visit.append((current_node.left, current_level + 1))

            if current_node.right:
                to_visit.append((current_node.right, current_level + 1))

            result.append(current_node.val)

        return "".join(result)


if __name__ == "__main__":
    tree = Node("a")
    tree.left = Node("b")
    tree.right = Node("c")
    tree.left.left = Node("d")
    tree.left.right = Node("e")
    tree.right.left = Node("f")
    tree.right.right = Node("g")

    print(tree)
