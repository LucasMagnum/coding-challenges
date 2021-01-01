"""
Level of tree with Maximum Sum

This problem was recently asked by Microsoft:

Given a binary tree, find the level in the tree where the sum of all nodes on that level is the greatest.

"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"(Value: {self.value} Left: {self.left} Right: {self.right})"


def tree_level_max_sum(root):
    to_visit = [(root, 0)]
    sum_by_level = []

    while to_visit:
        current, level = to_visit.pop()

        if len(sum_by_level) == level:
            sum_by_level.append(0)

        sum_by_level[level] += current.value

        if current.left:
            to_visit.append((current.left, level + 1))

        if current.right:
            to_visit.append((current.right, level + 1))

    return max(enumerate(sum_by_level), key=lambda args: args[1])


def recursive_solution(root):
    def calculate_sum(root, level, sum_by_level):
        if not root:
            return

        sum_by_level[level] = sum_by_level.get(level, 0) + root.value
        calculate_sum(root.left, level + 1, sum_by_level)
        calculate_sum(root.right, level + 1, sum_by_level)

    sum_by_level = {}
    calculate_sum(root, 0, sum_by_level)

    return max(sum_by_level.items(), key=lambda args: args[1])


if __name__ == "__main__":
    n3 = Node(4, Node(3), Node(2))
    n2 = Node(5, Node(4), Node(-1))
    n1 = Node(1, n2, n3)

    """
         1          Level 0 - Sum: 1
        / \
       4   5        Level 1 - Sum: 9
      / \ / \
     3  2 4 -1      Level 2 - Sum: 8
    """

    print(tree_level_max_sum(n1))
    print(recursive_solution(n1))
    # Should print 1 as level 1 has the highest level sum
