"""
Intersection:

    Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
    node. Note that the intersection is defined based on reference, not value. That is, if the kth
    node of the first linked list is the exact the same node (by reference) as the jth node of the second linked
    list, then they are intersecting.
"""

from data import create_list, Node


def brute_force_solution(first, second):
    """Naive solution comparing each pair of nodes."""
    while first:
        second_head = second

        while second_head:
            if second_head is first:
                return second_head

            second_head = second_head.next

        first = first.next

    return


def count_and_compare_solution(first, second):
    if not first or not second:
        return None

    first_tail, first_size = _get_tail_and_size(first)
    second_tail, second_size = _get_tail_and_size(second)

    # If they intersect they both will have the same last node
    if first_tail is not second_tail:
        return None

    shorter, longer = (first, second) if first_size < second_size else (second, first)

    # Advance pointer for longer list
    longer = _get_kth_node(longer, abs(first_size - second_size))

    # Move both pointer until collision
    while (shorter != longer):
        shorter = shorter.next
        longer = longer.next

    return longer


def _get_tail_and_size(node):
    count = 1

    while node.next:
        count += 1
        node = node.next

    return node, count


def _get_kth_node(node, kth):
    while kth > 0 and node:
        node = node.next
        kth -= 1
    return node


def insert_after(head, value, node):
    while head:
        if head.val == value:
            head.next = node
        head = head.next


if __name__ == "__main__":
    first = create_list([0, 1, 2, 3, 4, 5, 6, 7])
    second = create_list([11, 12, 13, 14])

    intersecting_node = Node(-1)
    intersecting_node.next = Node(-2)
    intersecting_node.next.next = Node(-3)
    insert_after(first, 7, intersecting_node)
    insert_after(second, 14, intersecting_node)

    print(f"Solution({first}, {second}) -> ", brute_force_solution(first, second))
    print(f"Solution({first}, {second}) -> ", count_and_compare_solution(first, second))