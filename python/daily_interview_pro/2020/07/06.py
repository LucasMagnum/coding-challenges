"""
Sudoku Check

This problem was recently asked by Facebook:

A Sudoku board is a 9x9 grid, where each row, column and each 3x3 subbox
contains the number from 1-9. Here's an example of a Sudoku board.
-------------
|534|678|912|
|672|195|348|
|198|342|567|
|------------
|859|761|423|
|426|853|791|
|713|924|856|
|------------
|961|537|284|
|287|419|635|
|345|286|179|
|------------

Given a 9x9 board, determine if it is a valid Sudoku board. The board may be partially filled,
where an empty cell will be represented by the space character ' '.
"""


def validate_sudoku(board):
    if len(board) != 9:
        return False

    for row in board:
        if len(row) != 9:
            return False

        seen = [False] * 10
        for column in row:
            if column == " ":
                continue

            if seen[column]:
                return False

            seen[column] = True

    for col_idx in range(9):
        seen = [False] * 10
        for row_idx in range(9):
            cell = board[col_idx][row_idx]

            if cell == " ":
                continue

            if seen[cell]:
                return False
            seen[cell] = True

    for i in range(3):
        for j in range(3):
            seen = [False] * 10

            for x in range(3):
                for y in range(3):
                    cell = board[i * 3 + x][j * 3 + y]
                    if cell == " ":
                        continue

                    if seen[cell]:
                        return False
                    seen[cell] = True
    return True


board = [
    [5, " ", 4, 6, 7, 8, 9, 1, 2],
    [6, " ", 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]

if __name__ == "__main__":
    print(validate_sudoku(board))
    # True
