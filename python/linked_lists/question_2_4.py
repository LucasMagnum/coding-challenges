"""
Partition:

    Write code to partition a linked list around a value X, such that
    all nodes less than X come before all nodes greater than or equal to X.
    (Important: the partition element X can appear anywhere in the "right partition";
    it does not need to appear between the left and right partitions.)

    Ex:

        Input: 3 - 5 - 8 - 5 - 10 - 2 - 1 [partition = 5]
        Output: 3 - 1 - 2       ->  10 - 5 - 5 - 8

"""

from data import Node


def stable_solution(node, partition_by):
    """Stable solution keeps the nodes in their original order."""
    before_start = None
    before_end = None

    after_start = None
    after_end = None

    while node:
        next_node, node.next = node.next, None

        if node.val < partition_by:
            if before_start is None:
                before_start = node
                before_end = before_start
            else:
                before_end.next = node
                before_end = node

        else:
            if after_start is None:
                after_start = node
                after_end = after_start
            else:
                after_end.next = node
                after_end = node

        node = next_node

    if before_start is None:
        return after_start

    before_end.next = after_start
    return before_start


def not_stable_solution(node, partition_by):
    head, tail = node, node

    while node:
        next_node = node.next

        if node.val < partition_by:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next_node

    tail.next = None
    return head


def create_list():
    linked_list = Node(3)

    node = linked_list
    for x in [1, 8, 5, 10, 2, 1]:
        new_node = Node(x)
        node.next = new_node
        node = new_node
    return linked_list

if __name__ == "__main__":

    linked_list = create_list()
    print(f"Solution({linked_list}) ->", stable_solution(linked_list, 5))

    linked_list = create_list()
    print(f"Solution({linked_list}) ->", not_stable_solution(linked_list, 5))

