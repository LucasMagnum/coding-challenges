"""
Reshaping Matrix

This problem was recently asked by Facebook:

Reshaping a matrix means to take the same elements in a matrix but change the row and column length.
This means that the new matrix needs to have the same elements filled in the
same row order as the old matrix.

Given a matrix, a new row size x and a new column size y, reshape the matrix.
If it is not possible to reshape, return None.

"""


def reshape_matrix(mat, x, y):
    if len(mat) * len(mat[0]) != x * y:
        return None

    new_mat = [[0] * x for _ in range(y)]

    i = 0
    j = 0
    for row in mat:
        for cell in row:
            new_mat[i][j] = cell

        j += 1

        if j >= x:
            i += 1
            j = 0

    return new_mat


if __name__ == "__main__":
    print(reshape_matrix([[1, 2], [3, 4]], 1, 4))
    # [[1], [2], [3], [4]]

    print(reshape_matrix([[1, 2], [3, 4]], 2, 3))
    # None