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


def solution(linked_list):
    if not linked_list:
        return

    current = linked_list
    while current:
        if current.next and current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return linked_list

if __name__ == "__main__":
    linked_list = Node(1, Node(1, Node(1, Node(2, Node(3, Node(3, Node(4, Node(4, Node(4)))))))))
    print(linked_list)
    # 1 2 3 3 4
    solution(linked_list)
    print(linked_list)
    # 1 2 4

