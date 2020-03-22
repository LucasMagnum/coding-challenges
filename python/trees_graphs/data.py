class TreeNode:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

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
