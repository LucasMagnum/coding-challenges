"""
Paths with Sum:

You are given a binary tree in which each node contains an integer value (which might be positive or negative). Design an algorithm to count the number of paths
that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes)
"""
from data import TreeNode


def solution(root, target, running_sum, path_count):
    if not root:
        return 0

    running_sum += root.value
    total = running_sum - target
    total_paths = path_count.get(total, 0)

    # If running sum equals to target, them one additional path starts at root
    if running_sum == target:
        total_paths += 1

    # Increment path count, recurse, them decrement path count
    increment_path_count(path_count, running_sum, 1)
    total_paths += solution(root.left, target, running_sum, path_count)
    total_paths += solution(root.right, target, running_sum, path_count)
    increment_path_count(path_count, running_sum, -1)

    return total_paths


def increment_path_count(path_count, key, delta):
    new_count = path_count.get(key, 0) + delta
    if new_count == 0:
        del path_count[key]
    else:
        path_count[key] = new_count


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(3, left=TreeNode(3), right=TreeNode(-2))
    root.left.right = TreeNode(1, right=TreeNode(2))
    root.right = TreeNode(-3, right=TreeNode(11))

    print("Solution", solution(root, 8, 0, {}))
