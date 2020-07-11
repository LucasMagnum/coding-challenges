"""
Queens on a chessboard

This problem was recently asked by Microsoft:

N-Queens is the problem where you find a way to put N queens on a
NxN chess board without them being able to attack each other.

Given an integer N, return 1 possible solution by returning all the queen's position.

"""


def n_queens(n):
    col = [True] * n
    row = [True] * n
    asc_diag = [True] * (n * 2 - 1)
    desc_diag = [True] * (n * 2 - 1)
    return helper(n, col, row, asc_diag, desc_diag)


def helper(n, col, row, asc_diag, desc_diag, queen_pos=[]):
    if len(queen_pos) == n:
        return queen_pos

    curr_row = len(queen_pos)
    for curr_col in range(n):
        if col[curr_col] and asc_diag[curr_row + curr_col] and desc_diag[curr_row - curr_col]:
            col[curr_col] = False
            asc_diag[curr_row + curr_col] = False
            desc_diag[curr_row - curr_col] = False
            queen_pos.append((curr_row, curr_col))
            queen_pos = helper(n, col, row, asc_diag, desc_diag, queen_pos)

            if len(queen_pos) == n:
                return queen_pos

            # backtrack
            col[curr_col] = True
            asc_diag[curr_row + curr_col] = True
            desc_diag[curr_row - curr_col] = True
            queen_pos.pop()

    return queen_pos


if __name__ == "__main__":
    print(n_queens(5))
    # There can be many answers
    # [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]

    # Q . . . .
    # . . . Q .
    # . Q . . .
    # . . . . Q
    # . . Q . .