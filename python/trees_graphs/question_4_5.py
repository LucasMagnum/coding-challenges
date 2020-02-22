"""
Validate BST
    Implement a function to check if a binary tree is a binary search tree.
"""


class TreeNode:
    def __init__(self, value, parent, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = left

    def __str__(self):  
        return f"{self.value}"


def build_tree(array, start, end, parent=None):
    if end < start:
        return

    mid = (start + end) // 2

    node = TreeNode(array[mid], parent)
    node.left = build_tree(array, start, mid - 1, node)
    node.right = build_tree(array, mid + 1, end, node)

    return node


def is_bst_copying_solution(tree, array=None, index=0):
    array = copy_bst(tree, array)
    for index in range(1, len(array) - 1):
        if array[index] <= array[index - 1]:
            return False
    return True


def is_bst_recursive_solution(tree, min_value=None, max_value=None):
    if not tree:
        return True
    
    if (
        min_value is not None and tree.value <= min_value or
        max_value is not None and tree.value > max_value
    ):
        return False
    
    if (
        not is_bst_recursive_solution(tree.left, min_value, tree.value) or
        not is_bst_recursive_solution(tree.right, tree.value, max_value)
    ):
        return False
    
    return True


def copy_bst(tree, array=None):
    if not tree:
        return

    if array is None:
        array = []

    copy_bst(tree.left, array)
    array.append(tree.value)
    copy_bst(tree.right, array)
    return array


if __name__ == "__main__":
    tree = build_tree(list(range(0, 101)), 0, 99)
    print("Solution -> ", is_bst_copying_solution(tree))
    print("Solution -> ", is_bst_recursive_solution(tree))