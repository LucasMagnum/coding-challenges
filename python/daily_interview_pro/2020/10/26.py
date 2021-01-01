"""
Intersection of Linked Lists

This problem was recently asked by Apple:

You are given two singly linked lists. The lists intersect at some node. Find, and return the node. Note: the lists are non-cyclical.

Example:

A = 1 -> 2 -> 3 -> 4
B = 6 -> 3 -> 4

This should return 3 (you may assume that any nodes with the same value are the same node).

"""
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def show(self):
        c = self
        while c:
            print(c.val, end=", ")
            c = c.next


def intersection(a, b):
    length_a = length(a)
    length_b = length(b)

    diff = abs(length_a - length_b)
    slower, faster = (a, b) if length_a < length_b else (b, a)

    for _ in range(diff):
        faster = faster.next

    while slower != faster:
        slower = slower.next
        faster = faster.next

    if not slower or not faster:
        return Node(-1)

    return slower


def length(node):
    count = 0

    while node:
        node = node.next
        count += 1

    return count


if __name__ == "__main__":
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)

    b = Node(6)
    b.next = a.next.next

    c = intersection(a, b)
    c.show()
    # 3 4