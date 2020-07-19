"""
Rotate Linked List

This problem was recently asked by AirBNB:

Given a linked list and a number k, rotate the linked list by k places.

"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        current = self
        ret = ""
        while current:
            ret += str(current.value)
            current = current.next
        return ret


def rotate_list(linked_list, k):
    length = 0
    current = linked_list

    while current:
        length += 1
        current = current.next

    k = k % length
    fast, slow = linked_list, linked_list

    for _ in range(k):
        fast = fast.next

    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    fast.next = linked_list
    head = slow.next
    slow.next = None
    return head


if __name__ == "__main__":
    # Order is 1, 2, 3, 4
    llist = Node(1, Node(2, Node(3, Node(4))))

    # Order should now be 3, 4, 1, 2
    print(rotate_list(llist, 2))
    # 3412
