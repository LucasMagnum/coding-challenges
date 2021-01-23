"""
This problem was recently asked by Uber:

Given a linked list, determine if the linked list has a cycle in it.
For notation purposes, we use an integer pos which represents the zero-indexed
position where the tail connects to.

Example:
Input: head = [4,3,2,1,0], pos = 1.
Output: true

"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def solution(head):
    slow, fast = head, head

    if fast.next:
        fast = fast.next.next

    while fast.next:
        if slow is fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False


if __name__ == "__main__":
    testHead = ListNode(4)
    node1 = ListNode(3)
    testHead.next = node1
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(1)
    node2.next = node3
    testTail = ListNode(0)
    node3.next = testTail
    testTail.next = node1
    print(solution(testHead))
    # True