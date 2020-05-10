"""
Detect Linked List Cycle

This problem was recently asked by Uber:

Given a linked list, determine if the linked list has a cycle in it.
For notation purposes, we use an integer pos which represents the zero-indexed position where the tail connects to.

"""

class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None


def dict_solution(head):
    values = {}

    while head:
        if head.val in values:
            return True
        values[head.val] = True
        head = head.next

    return False


def solution(head):
    """
    One simple solution is to reverse the linked list. 
    If the new head of the reversed list is the same as the head of the input list, 
    that means that the list has a cycle, 
    since the reversed list would always end up pointing to the previous value of the cycle node, 
    which ultimately ends up as the initial head.
    If the new head is different, there was no cycle.
    """
    if not head or not head.next:
        return False

    reverse_head = reverse_list(head)
    return reverse_head is head


def reverse_list(head):
    new_head = None

    while head:
        tmp = head.next
        head.next = new_head
        new_head = head
        head = tmp
    
    return new_head


if __name__ == "__main__":
    head = ListNode(4)
    node1 = ListNode(3)
    head.next = node1
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(1)
    node2.next = node3
    tail = ListNode(0)
    node3.next = tail
    tail.next = node3

    print(dict_solution(head))
    print(solution(head))