"""
Delete Middle Node:
    Implement an algorithm to delete a node in the middle (i.e, any node but the first and last node, not
    necessarily the exact middle) of a singly linked list, given only access to that node.

    Example:

    Input: node C from A -> B -> C -> D -> E -> F
    Output: A -> B -> D -> E -> F
"""

from data import Node


def solution(node):
    if node and node.next:
        node.val = node.next.val
        node.next = node.next.next
    return node


if __name__ == "__main__":
    linked_list = Node("head")

    node = linked_list
    selected_node = None
    for x in ["A", "B", "C", "D", "E", "F"]:
        new_node = Node(x)

        if x == "C":
            selected_node = new_node

        node.next = new_node
        node = new_node

    print(f"Solution({linked_list}) ->", )
    solution(selected_node)
    print(linked_list)
