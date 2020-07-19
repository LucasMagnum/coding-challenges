"""
Remove Duplicate from Linked List

This problem was recently asked by Amazon:

Given a sorted linked list of integers, remove all the duplicate elements in
the linked list so that all elements in the linked list are unique.

"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"({self.value}, {self.next})"


def remove_dup(linked_list):
    current = linked_list

    while current and current.next:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next

    return linked_list


if __name__ == "__main__":
    linked_list = Node(1, Node(2, Node(2, Node(3, Node(3)))))
    remove_dup(linked_list)
    print(linked_list)
    # (1, (2, (3, None)))
