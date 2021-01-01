"""
Flatten Binary Tree

This problem was recently asked by Amazon:

Given a binary tree, flatten the binary tree using inorder traversal.
Instead of creating a new list, reuse the nodes, where the list is represented by
following each right child. As such the root should always be the first element in
the list so you do not need to return anything in the implementation,
just rearrange the nodes such that following the right child will give us the list.

"""


class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    return f"({self.value}, {self.left}, {self.right})"


def flatten_bst(root):
    if root is None:
        return root

    right_node = root.right
    end_node = root

    if root.left:
        begin_node, end_node = flatten_bst(root.left)
        root.left = None
        end_node.right = root.right
        root.right = begin_node

    if right_node:
        _, end_node = flatten_bst(root.right)

    return root, end_node


if __name__ == "__main__":
    n5 = Node(5)
    n4 = Node(4)
    n3 = Node(3, n4)
    n2 = Node(2, n5)
    n1 = Node(1, n2, n3)

    #      1
    #    /   \
    #   2     3
    #  /     /
    # 5     4

    flatten_bst(n1)
    print(n1)

    # n1 should now look like
    #   1
    #    \
    #     2
    #      \
    #       5
    #        \
    #         3
    #          \
    #           4