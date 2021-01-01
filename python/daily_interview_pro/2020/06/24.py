"""
Picking up Change

This problem was recently asked by Amazon:

Given a 2d n x m matrix where each cell has a certain amount of change on the floor,
your goal is to start from the top left corner mat[0][0] and end in the bottom right corner mat[n - 1][m - 1]
with the most amount of change. You can only move either left or down.

"""


def solution(mat):
    max_change_mat = []
    for i, row in enumerate(mat):
        max_change_mat.append([0] * len(row))
        for j, cell in enumerate(row):
            if j > 0:
                max_change_mat[i][j] = max(
                    max_change_mat[i][j - 1] + mat[i][j], max_change_mat[i][j]
                )
            if i > 0:
                max_change_mat[i][j] = max(
                    max_change_mat[i - 1][j] + mat[i][j], max_change_mat[i][j]
                )

    return max_change_mat[-1][-1]


if __name__ == "__main__":
    matrix = [[0, 3, 0, 2], [1, 2, 3, 3], [6, 0, 3, 2]]
    print(solution(matrix))
