"""
Searching a Matrix

This problem was recently asked by Facebook:

Given a matrix that is organized such that the numbers will always be sorted left to right,
and the first number of each row will always be greater than the last element of the last row
(mat[i][0] > mat[i - 1][-1]), search for a specific value in the matrix and return whether it exists.

"""


def search_matrix(matrix, value):
    if len(matrix) == 0:
        return False

    row_len = len(matrix)
    col_len = len(matrix[0])

    low = 0
    high = row_len * col_len

    while low < high:
        mid = (low + high) // 2

        if matrix[mid // col_len][mid % col_len] == value:
            return True
        elif matrix[mid // col_len][mid % col_len] < value:
            low = mid + 1
        else:
            high = mid

    return False



if __name__ == "__main__":
    matrix = [
        [1, 3, 5, 8],
        [10, 11, 15, 16],
        [24, 27, 30, 31],
    ]

    print(search_matrix(matrix, 4))
    # False

    print(search_matrix(matrix, 10))
    # True
