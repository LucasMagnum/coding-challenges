"""
Create a balanced binary search tree

This problem was recently asked by LinkedIn:

Given a sorted list of numbers, change it into a balanced binary search tree. You can assume there will be no duplicate numbers in the list.
"""

from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        # level-by-level pretty-printer
        nodes = deque([self])
        answer = ""
        while len(nodes):
            node = nodes.popleft()
            if not node:
                continue
            answer += str(node.value)
            nodes.append(node.left)
            nodes.append(node.right)
        return answer


def solution(array):
    def build_tree(start, end):
        if end < start:
            return

        mid = (start + end) // 2

        node = Node(array[mid])
        node.left = build_tree(start, mid - 1)
        node.right = build_tree(mid + 1, end)
        return node

    return build_tree(0, len(array) - 1)


if __name__ == "__main__":
    print(solution([1, 2, 3, 4, 5, 6, 7]))  #  4261357
