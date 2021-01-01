"""
Add two numbers as a linked list

This problem was recently asked by Microsoft:

You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def recursive_solution(l1, l2, carry):
    total = l1.val + l2.val + carry
    carry = total // 10

    result_node = ListNode(total % 10)

    if l1.next or l2.next or carry:
        if not l1.next:
            l1.next = ListNode(0)

        if not l2.next:
            l2.next = ListNode(0)

        result_node.next = recursive_solution(l1.next, l2.next, carry)

    return result_node


def iterative_solution(l1, l2):
    first = l1
    second = l2
    carry = 0

    result_head = None
    current = None

    while first or second:
        total = first.val + second.val + carry
        carry = total // 10

        if not current:
            current = ListNode(total % 10)
            result_head = current
        else:
            current.next = ListNode(total % 10)
            current = current.next

        if first.next or second.next:
            first.next = first.next if first.next else ListNode(0)
            second.next = second.next if second.next else ListNode(0)

        first = first.next
        second = second.next

    return result_head


if __name__ == "__main__":
    l1 = ListNode(0)
    l1.next = ListNode(0)
    l1.next.next = ListNode(9)

    l2 = ListNode(0)
    l2.next = ListNode(0)
    l2.next.next = ListNode(1)

    result = recursive_solution(l1, l2, 0)

    print("Recursive")
    while result:
        print(result.val, end=" ")
        result = result.next

    print()
    print("Iterative")
    result = iterative_solution(l1, l2)
    while result:
        print(result.val, end=" ")
        result = result.next
