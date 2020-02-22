"""
Reverse a Linked List

This problem was recently asked by Google:

Given a singly-linked list, reverse the list. This can be done iteratively or recursively.
Can you get both solutions?

Example:
Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL

"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def print(self):
        node = self
        output = ""
        while node is not None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

    def reverse_iteratively(self, head):
        previous = None

        while head:
            next_node, head.next = head.next, previous
            previous, head = head, next_node

        return head

    def reverse_recursively(self, head):
        if not head or not head.next:
            return head

        node = self.reverse_recursively(head.next)

        head.next.next = head
        head.next = None
        return node


# Test Program
# Initialize the test list:
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.print()
# 4 3 2 1 0
#testHead.reverse_iteratively(testHead)
testHead.reverse_recursively(testHead)

print("List after reversal: ")
testTail.print()
# 0 1 2 3 4
