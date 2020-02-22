"""
Loop Detection

    Given a linked list which might contain a loop, implement an algorithm that returns
    the node at the begining of the loop (if one exists)

"""

from data import create_list, Node


def hashset_solution(linked_list):
    seen = set()

    while linked_list:
        if id(linked_list) in seen:
            return linked_list.val

        seen.add(id(linked_list))
        linked_list = linked_list.next

    return None


def fast_runner_solution(linked_list):
    slow = linked_list
    fast = linked_list

    # Find collision point (LOOP_SIZE - K)
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            break

    # Error check (no meeting point)
    if not fast or not fast.next:
        return None

    # Move slow head, keep fast at meeting point, each are k steps from
    # the loop start. If they move at the same pace, they must meet at Loop start.
    slow = linked_list
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    # Both now point to the start at the loop
    return fast.val



if __name__ == "__main__":
    with_loop = create_list(range(10, 1000000))
    no_loop = create_list([11, 12, 13, 14, 16, 17, 18, 19, 20])

    head = with_loop
    while head.next:
        head = head.next
    head.next = with_loop

    print(f"Solution(with_loop) -> ", hashset_solution(with_loop))
    print(f"Solution({no_loop}) -> ", hashset_solution(no_loop))

    print(f"Solution(with_loop) -> ", fast_runner_solution(with_loop))
    print(f"Solution({no_loop}) -> ", fast_runner_solution(no_loop))