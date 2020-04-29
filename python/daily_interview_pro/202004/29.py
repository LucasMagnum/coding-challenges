"""
Determine If Linked List is Palindrome

This problem was recently asked by Microsoft:

You are given a doubly linked list. Determine if it is a palindrome.

Can you do this for a singly linked list?


"""

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def solution(node):
    nodes = []

    while node:
        nodes.append(node.val)
        node = node.next

    return nodes == nodes[::-1]


if __name__ == "__main__":
    node = Node('a')
    node.next = Node('b')
    node.next.prev = node
    node.next.next = Node('b')
    node.next.next.prev = node.next
    node.next.next.next = Node('a')
    node.next.next.next.prev = node.next.next
    print(solution(node))