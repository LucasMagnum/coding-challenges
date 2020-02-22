"""
Rotate Matrix

    Given an image represented by an N X N matrix, where each pixel in the image is
    represented by an integer, write a method to rotate the image by 90 degrees.

    Can you do this in place?
"""


def solution(matrix):
    size = len(matrix)

    layer = 0
    while layer < size / 2:
        first = layer
        last = size - 1 - layer

        for i in range(first, last):
            offset = i - first

            top = matrix[first][i]

            # left -> top
            matrix[first][i] = matrix[last - offset][first]

            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right > bottom
            matrix[last][last - offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top

        layer += 1

    return matrix



if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    print("Rotate matrix({matrix}) ->", solution(matrix))