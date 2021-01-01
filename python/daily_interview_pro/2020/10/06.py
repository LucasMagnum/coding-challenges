"""

Intersection of Linked Lists


You are given two singly linked lists.
The lists intersect at some node. Find, and return the node.

Note: the lists are non-cyclical.

Example:

A = 1 -> 2 -> 3 -> 4
B = 6 -> 3 -> 4

This should return 3 (you may assume that any nodes with the same value are the same node).


"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def prettyPrint(self):
        c = self
        while c:
            print(c.val, end=" ")
            c = c.next


def intersection(first, second):
    first_len, second_len = length(first), length(second)

    smaller, bigger = (first, second) if first_len < second_len else (second, first)

    # Advance bigger
    for _ in range(abs(first_len - second_len)):
        bigger = bigger.next

    while smaller != bigger:
        smaller = smaller.next
        bigger = bigger.next

    return smaller


def length(node):
    if not node:
        return 0

    return 1 + length(node.next)


if __name__ == "__main__":
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)

    b = Node(6)
    b.next = a.next.next

    c = intersection(a, b)
    c.prettyPrint()
    # 3 4
