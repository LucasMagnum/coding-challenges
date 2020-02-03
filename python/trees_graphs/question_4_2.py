"""
Minimal Tree:
    Given a sorted (increasing order) array with unique integer elements, 
    write an algorithm to create a binary search tree with minimal height.
"""

def dfs(node):
    if not node:
        return

    dfs(node.left)
    print(node, end=", ")
    dfs(node.right)


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = left

    def __str__(self):  
        return f"{self.value}"


def minimal_tree(array, start, end):
    if end < start:
        return

    mid = (start + end) // 2

    node = TreeNode(array[mid])
    node.left = minimal_tree(array, start, mid - 1)
    node.right = minimal_tree(array, mid + 1, end)

    return node


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    tree = minimal_tree(array, 0, len(array) - 1)
    print(f"Solution({array}) -> ", )
    dfs(tree)