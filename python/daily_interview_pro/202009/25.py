"""
Add two numbers as a linked list

This problem was recently asked by Microsoft:

You are given two linked-lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""


class Node(object):
  def __init__(self, x):
    self.val = x
    self.next = None


def solution(l1, l2, carry = 0):
    value = l1.val + l2.val + carry
    carry = value // 10
    result = Node(value % 10)

    if l1.next != None or l2.next != None:
        if not l1.next:
            l1.next = Node(0)

        if not l2.next:
            l2.next = Node(0)

        result.next = solution(l1.next, l2.next, carry)

    return result


def iterative_solution(l1, l2):
    carry = 0
    result = current = None

    while l1 or l2:
        value = l1.val + l2.val + carry
        carry = value // 10

        if not current:
            result = current = Node(value % 10)
        else:
            current.next = Node(value % 10)
            current = current.next

        if l1.next or l2.next:
            if not l1.next:
                l1.next = Node(0)

            if not l2.next:
                l2.next = Node(0)

        l1 = l1.next
        l2 = l2.next

    return result


if __name__ == "__main__":
    l1 = Node(2)
    l1.next = Node(4)
    l1.next.next = Node(3)

    l2 = Node(5)
    l2.next = Node(6)
    l2.next.next = Node(4)

    result = solution(l1, l2)
    while result:
        print(result.val, end=" ")
        result = result.next
    # 7 0 8
