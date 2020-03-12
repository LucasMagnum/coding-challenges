"""
Check Subtree

T1 and T2 are two very large binary trees, with T1 much bigger than T2.
Create an algorithm to determine if T2 is a subtree of T1.

A tree T2 is a subtree of T1 if there exists a node in T1 such that the subtree
of N is identical to T2.

That is, if you cut off the tree at node N, the two trees would be identical.

"""

from data import TreeNode, build_tree


def is_subtree(larger, smaller):
    # The empty subtree is always a subtree
    if not smaller:
        return True

    # Big tree empty and subtree still not found
    if not larger:
        return False

    if larger.value == smaller.value and match_tree(larger, smaller):
        return True

    return is_subtree(larger.left, smaller) or is_subtree(larger.right, smaller)


def match_tree(larger, smaller):
    # Nothing left in the subtree
    if not larger and not smaller:
        return True

    # Exactly one tree is empty, therefore trees do not match
    if not larger or not smaller:
        return False

    # Data does not match
    if larger.value != smaller.value:
        return False

    return match_tree(larger.left, smaller.left) and match_tree(larger.right, smaller.right)


if __name__ == "__main__":
    larger = build_tree(range(0, 1000), 0, 999)
    # Create a smaller tree matching a root from larger tree
    smaller = build_tree(range(0, 249), 0, 248)

    print(is_subtree(larger, smaller))