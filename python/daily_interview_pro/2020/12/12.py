"""
Transpose Matrix

This problem was recently asked by Twitter:

Given a matrix, transpose it. Transposing a matrix means the rows are now the column and vice-versa.

"""

def transpose(mat):
    if len(mat) == 0:
        return []

    new_mat = [[0] * len(mat) for _ in range(len(mat[0]))]

    for x, row in enumerate(mat):
        for y, cell in enumerate(row):
            new_mat[y][x] = cell

    return new_mat


if __name__ == "__main__":
    mat = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    print(transpose(mat))
    # [[1, 4],
    #  [2, 5],
    #  [3, 6]]