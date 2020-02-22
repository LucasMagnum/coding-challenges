"""
Return Kth to Last

    Implement an algorithm to find the kth to last element of a singly linked list.
"""

from data import Node


def solution(head, kth):
    """This solution returns only the index of the kth node"""
    if head is None:
        return 0

    index = solution(head.next, kth) + 1
    if (index == kth):
        print(f"{kth}th to last node is ", head.val)
    return index


def node_solution(head, kth):
    """This solution returns the node recursively,
    it wraps the function so we can the counter outside"""
    index = 0

    def wrapp_func(head, kth):
        nonlocal index

        if head is None:
            return

        node = wrapp_func(head.next, kth)
        index = index + 1

        if (index == kth):
            return head

        return node

    return wrapp_func(head, kth)


def iterative_solution(head, kth):
    """Use two pointers strategy"""
    current = head
    runner = head

    for _ in range(kth):
        if runner is None:
            return None

        runner = runner.next

    # Move both at same pace, when runner hits the end
    # current will be the answer
    while (runner is not None):
        runner = runner.next
        current = current.next

    return current


if __name__ == "__main__":
    linked_list = Node("head")

    node = linked_list
    for x in [1, 2, 3, 4, 5, 2, 3, 1, 7]:
        new_node = Node(x)
        node.next = new_node
        node = new_node

    kth = 3
    print(f"Solution({linked_list}, {kth}) ->", solution(linked_list, kth))
    print(f"Solution({linked_list}, {kth}) ->", node_solution(linked_list, kth))
    print(f"Solution({linked_list}, {kth}) ->", iterative_solution(linked_list, kth))