"""
Sum lists:

    You have two numbers represented by a linked list, where each node contains
    a single digit. The digits are stored in reverse order, such that
    the 1's digit is at the head of the list. Write a function
    that adds the two numbers and returns the sum as a linked list.
    (You are not allowed to "cheat" and just convert the linked list to an integer)

    Ex:
        Input: 7 - 1 - 6 + 5 - 9 - 2 (617 + 295)
        Output: 2 - 1 - 9

    Follow up: Suppose the digits are stored in foward order. Repeat the above problem.
        Input: 6 - 1 - 7 + 5 - 9 - 2 (617 + 295)
        Output: 9 - 1 - 2

"""
from data import Node, create_list


def backward_solution(first, second, carry=0):
    if first is None and second is None and carry == 0:
        return None

    result = Node(None)
    value = carry

    if first is not None:
        value += first.val

    if second is not None:
        value += second.val

    # Last digit of number
    result.val = value % 10

    if (first is not None or second is not None):
        next_node = backward_solution(
            first and first.next,
            second and second.next,
            1 if value >= 10 else 0
        )
        result.next = next_node

    return result


def forward_solution(first, second):
    pass



if __name__ == "__main__":

    first, second = create_list([7, 1, 6]), create_list([5, 9])
    print(f"Solution({first} + {second}) ->", backward_solution(first, second))

    first, second = create_list([7, 1, 6]), create_list([5, 9, 2])
    print(f"Solution({first} + {second}) ->", forward_solution(first, second))
