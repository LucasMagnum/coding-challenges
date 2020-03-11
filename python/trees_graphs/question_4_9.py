"""
BST Sequences

A binary search tree was created by traversing through an array
from left to right and inserting each element.

Given a binary search tree with distinct elements, print all possible arrays
that cold have led to this tree.

"""

from data import TreeNode, build_tree


def solution(node):
    result = []

    if not node:
        result.append([])
        return result

    prefix = []
    prefix.append(node.value)

    left_sequence = solution(node.left)
    right_sequence = solution(node.right)

    for left in left_sequence:
        for right in right_sequence:
            weaved = []
            weave_lists(left, right, weaved, prefix)
            result.extend(weaved)

    return result


def weave_lists(first, second, results, prefix):
    if not first or not second:
        result = prefix[:]
        result.extend(first)
        result.extend(second)
        results.append(result)
        return results

    head = first.pop(0)
    prefix.append(head)
    weave_lists(first, second, results, prefix)
    prefix.pop()
    first.insert(0, head)

    head_second = second.pop(0)
    prefix.append(head_second)
    weave_lists(first, second, results, prefix)
    prefix.pop()
    second.insert(0, head)


if __name__ == "__main__":
    array = [3, 6, 7, 8, 12, 14, 16]
    tree = build_tree(array, 0, len(array) - 1)
    print(solution(tree))
