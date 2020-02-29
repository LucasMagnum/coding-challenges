"""
Remove k-th Last Element From Linked List

This problem was recently asked by AirBNB:

You are given a singly linked list and an integer k. Return the linked list, removing the k-th last element from the list.

Try to do it in a single pass and using constant space.
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return str(result)


def solution(head, k):
    slow, fast = head, head

    for i in range(k):
        fast = fast.next

    prev = None
    while fast:
        prev = slow
        slow = slow.next
        fast = fast.next

    if not prev:
        return slow.next

    prev.next = slow.next
    return head


if __name__ == "__main__":
    linked_list = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    print(f"Solution({linked_list}) ->", solution(linked_list, 3))