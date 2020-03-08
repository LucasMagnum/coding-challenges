"""
Intersection of Linked Lists

This problem was recently asked by Apple:

You are given two singly linked lists. The lists intersect at some node. Find, and return the node. Note: the lists are non-cyclical.

Example:

A = 1 -> 2 -> 3 -> 4
B = 6 -> 3 -> 4

This should return 3 (you may assume that any nodes with the same value are the same node).

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


def hashmap_solution(a: Node, b: Node):
    """The space complexity here is max(M, N)."""
    hashmap = {}

    while a:
        hashmap[id(a)] = a
        a = a.next

    while b:
        if id(b) in hashmap:
            return hashmap[id(b)]

        b = b.next

    return None


def solution(a: Node, b: Node):
    size_a, size_b = _length(a), _length(b)

    smaller, bigger = (a, b) if size_a < size_b else (b, a)

    # We run the bigger list by K,
    for _ in range(abs(size_a - size_b)):
        bigger = bigger.next

    while smaller != bigger:
        smaller = smaller.next
        bigger = bigger.next

    return smaller


def _length(node):
    if not node:
        return 0
    return 1 + _length(node.next)


if __name__ == "__main__":
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)

    b = Node(6)
    b.next = a.next.next

    print(f"Solution({a}, {b}) -> ", hashmap_solution(a, b))
    print(f"Solution({a}, {b}) -> ", solution(a, b))
