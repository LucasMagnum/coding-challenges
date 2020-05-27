"""
Generate Binary Search Trees

This problem was recently asked by Amazon:

Given a number n, generate all binary search trees that can be constructed with nodes 1 to n.

"""

class Node:
  def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

  def __str__(self):
        result = str(self.value)
        if self.left:
            result = result + str(self.left)
        if self.right:
            result = result + str(self.right)
        return result

def generate_bst(n):
    def helper(low, high):
        if low == high:
            return [None]

        bsts = []

        for x in range(low, high):
            left = helper(low, x)
            right = helper(x + 1, high)

            for l in left:
                for r in right:
                    bsts.append(Node(x, l, r))
        return bsts

    return helper(1, n + 1)


if __name__ == "__main__":
    for tree in generate_bst(3):
        print(tree)