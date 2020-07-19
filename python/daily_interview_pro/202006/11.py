"""
Maze Paths

This problem was recently asked by Microsoft:

A maze is a matrix where each cell can either be a 0 or 1.
A 0 represents that the cell is empty, and a 1 represents a wall that cannot be walked through.
You can also only travel either right or down.

Given a nxm matrix, find the number of ways someone can go from the top left corner to the bottom right corner.
You can assume the two corners will always be 0.

Example:
Input: [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
# 0 1 0
# 0 0 1
# 0 0 0
Output: 2

The two paths that can only be taken in the above example are:
down -> right -> down -> right, and down -> down -> right -> right.

"""


def solution(maze):
    paths = [[0] * len(maze[0]) for _ in range(len(maze))]
    paths[0][0] = 1

    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 1:
                continue

            if i > 0 and j > 0:
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
            elif i > 0:
                paths[i][j] = paths[i - 1][j]
            elif j > 0:
                paths[i][j] = paths[i][j - 1]

    return paths[-1][-1]


if __name__ == "__main__":
    print(solution([[0, 1, 0], [0, 0, 1], [0, 0, 0]]))
