"""
Making a Height Balanced Binary Search Tree

This problem was recently asked by Google:

Given a sorted list, create a height balanced binary search tree,
meaning the height differences of each node can only differ by at most 1.

tree = create_height_balanced_bst([1, 2, 3, 4, 5, 6, 7, 8])
# 53214768
#  (pre-order traversal)
#       5
#      / \
#     3    7
#    / \  / \
#   2   4 6  8
#  /
# 1

"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        answer = str(self.value)
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)
        return answer


def create_height_balanced_bst(nums):
    return build_tree(nums, 0, len(nums))


def build_tree(nums, low, high):
    if low == high:
        return None

    middle_index = int((low + high) / 2)
    root = Node(nums[middle_index])
    root.left = build_tree(nums, low, middle_index)
    root.right = build_tree(nums, middle_index + 1, high)
    return root


if __name__ == "__main__":
    print(create_height_balanced_bst([1, 2,  6, 8, 9 , 10]))