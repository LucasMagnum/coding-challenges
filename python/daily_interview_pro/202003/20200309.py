"""
This problem was recently asked by Twitter:

You are given an array of k sorted singly linked lists. Merge the linked lists into a single sorted linked list and return it.

"""


class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer


def brute_force(lists):
    array = []

    for head in lists:
        current = head
        while current:
            array.append(current.val)
            current = current.next

    new_head = current = Node(-1)
    for val in sorted(array):
        current.next = Node(val)
        current = current.next

    return new_head.next


def merge(lists):
    new_head = current = Node(-1)

    while any(lst is not None for lst in lists):
        current_min, i = min((lst.val, i) for i, lst in enumerate(lists) if lst is not None)
        lists[i] = lists[i].next
        current.next = Node(current_min)
        current = current.next

    return new_head.next


if __name__ == "__main__":
    a = Node(1, Node(3, Node(5)))
    b = Node(2, Node(4, Node(6)))
    print(merge([a, b]))
    print(brute_force([a, b]))