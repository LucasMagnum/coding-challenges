"""
Palindrome:
    Implement a function to check if a linked list is a palindrome.
"""

from data import create_list, Node


def solution_with_list(node):
    """
    This solution stores all the values of the linked list into a list and
    then check if it's palindrome.
    """
    data = []

    while node:
        data.append(node.val)
        node = node.next

    for first_index, last_index in zip(range(len(data)), range(len(data) - 1, 0, -1)):
        if last_index == first_index:
            break

        if data[first_index] != data[last_index]:
            return False

    return True


def reverse_and_compare(node):
    original_head = node

    # Reverse linked list
    reversed_head = None

    while node:
        new_node = Node(node.val)
        new_node.next = reversed_head

        reversed_head = new_node
        node = node.next

    # Compare
    while original_head or reversed_head:
        if original_head.val != reversed_head.val:
            return False

        original_head = original_head.next
        reversed_head = reversed_head.next

    return reversed_head is None and original_head is None


def solution_with_stack(node):
    """Create a stack insert until the middle and compare the rest."""
    fast, slow = node, node
    stack = []

    # Fast runs 2x faster than slow
    # slow will be in the middle when fast reaches the end
    while fast and fast.next:
        stack.append(slow.val)

        slow = slow.next
        fast = fast.next.next

    # Has odd number of elements, skip the middle
    if fast is not None:
        slow = slow.next

    while slow:
        if slow.val != stack.pop():
            return False

        slow = slow.next

    return True


def recursive_solution(node):
    length = _length_of_list(node)

    def is_palindrome(node, length):
        if node is None or length <= 0:
            return (node, True)
        elif length == 1:
            return (node.next, True)

        sub_node, result = is_palindrome(node.next, length - 2)

        # Child calls are not palindrome, pass back up the stack
        if not result or sub_node is None:
            return (sub_node, result)

        # Check if i matches n - i on the other side of the list
        return (sub_node.next, node.val == sub_node.val)

    _, result = is_palindrome(node, length)
    return result


def _length_of_list(node):
    count = 0

    while node:
        count += 1
        node = node.next

    return count


if __name__ == "__main__":
    is_palindrome = create_list(["r", "a", "c", "e", "c", "a", "r"])
    is_not_palindrome = create_list(["n", "o", "t", "p", "a", "l"])

    print(f"Solution({is_palindrome}) -> True ->", solution_with_list(is_palindrome))
    print(
        f"Solution({is_not_palindrome}) -> False ->",
        solution_with_list(is_not_palindrome),
    )

    print(f"Solution({is_palindrome}) -> True ->", reverse_and_compare(is_palindrome))
    print(
        f"Solution({is_not_palindrome}) -> False ->",
        reverse_and_compare(is_not_palindrome),
    )

    print(f"Solution({is_palindrome}) -> True ->", solution_with_stack(is_palindrome))
    print(
        f"Solution({is_not_palindrome}) -> False ->",
        solution_with_stack(is_not_palindrome),
    )

    print(f"Solution({is_palindrome}) -> True ->", recursive_solution(is_palindrome))
    print(
        f"Solution({is_not_palindrome}) -> False ->",
        recursive_solution(is_not_palindrome),
    )
