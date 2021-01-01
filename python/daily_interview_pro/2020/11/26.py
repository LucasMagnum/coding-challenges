"""
Remove Duplicate from Linked List

This problem was recently asked by Amazon:

Given a sorted linked list of integers, remove all the duplicate elements in the linked list so that all elements in the linked list are unique.


"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"({self.value}, {self.next})"


def remove_dup(lst):
    curr = lst

    while curr.next:
        if curr.value == curr.next.value:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return lst


if __name__ == "__main__":
    lst = Node(1, Node(2, Node(2, Node(3, Node(3)))))

    remove_dup(lst)
    print(lst)
    # (1, (2, (3, None)))