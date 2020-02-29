"""
Remove Consecutive Nodes that Sum to 0

This problem was recently asked by Uber:

Given a linked list of integers, remove all consecutive nodes that sum up to 0.

Example:

Input: 10 -> 5 -> -3 -> -3 -> 1 -> 4 -> -4
Output: 10

The consecutive nodes 5 -> -3 -> -3 -> 1 sums up to 0 so that sequence should be removed. 4 -> -4 also sums up to 0 too so that sequence should also be removed.

"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.value)
            current_node = current_node.next
        return str(result)


def solution(node: Node):
    dummy = Node(0, node)

    start = dummy
    while start:
        total = 0
        end = start.next

        while end:
            total += end.value

            if total == 0:
                start.next = end.next
                total = 0

            end = end.next
        start = start.next

    return dummy.next


if __name__ == "__main__":
    node = Node(6)
    node.next = Node(5)
    node.next.next = Node(-3)
    node.next.next.next = Node(-3)
    node.next.next.next.next = Node(1)
    node.next.next.next.next.next = Node(4)
    node.next.next.next.next.next.next = Node(-4)

    print(f"Solution({node}) ->", solution(node))