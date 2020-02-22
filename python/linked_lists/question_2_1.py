"""
Remove Dups

    Write code to remove duplicates from unsorted linked list.

    How would you solve this problem if a temporary buffer is not allowed?
"""

from data import Node


def buffer_solution(linked_list):
    seen = {}

    node = linked_list
    prev = None

    while node:
        if node.val in seen:
            prev.next = node.next

        else:
            prev = node
            seen[node.val] = True
        node = node.next

    return linked_list


def no_buffer_solution(linked_list):
    current = linked_list

    while current:

        runner = current
        while runner.next:
            if runner.next.val == current.val:
                runner.next = runner.next.next
            else:
                runner = runner.next

        current = current.next

    return linked_list


if __name__ == "__main__":
    linked_list = Node("head")

    node = linked_list
    for x in [1, 2, 3, 4, 5, 2, 3, 1, 7]:
        new_node = Node(x)
        node.next = new_node
        node = new_node

    print(f"Solution({linked_list})", buffer_solution(linked_list))
    print(f"Solution({linked_list})", no_buffer_solution(linked_list))
