"""
Remove duplicates from Linked List

This problem was recently asked by Twitter:

Given a linked list, remove all duplicate values from the linked list.

For instance, given 1 -> 2 -> 3 -> 3 -> 4, then we wish to return the linked list 1 -> 2 -> 4.

"""


class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self.next:
            return str(self.val)
        return str(self.val) + " " + str(self.next)


def solution(node):
    current = node

    while current:
        runner = current
        while runner.next:
            if runner.next.val == current.val:
                runner.next = runner.next.next
            else:
                runner = runner.next

        current = current.next

    return node


if __name__ == "__main__":
    n = Node(1, Node(2, Node(3, Node(3, Node(4)))))
    print(n)
    # 1 2 3 3 4
    solution(n)
    print(n)
    # 1 2 4
