"""
Rotate Matrix

This problem was recently asked by Uber:

Given a square 2D matrix (n x n), rotate the matrix by 90 degrees clockwise.

"""

def rotate(matrix):
    n = len(matrix)
    for i in range((len(matrix) + 1)//2):
        for j in range(i, len(matrix) - 1 - i):
            matrix[i][j], matrix[j][-i-1], matrix[-i-1][-j-1], matrix[-j -1][i] = matrix[-j-1][i], matrix[i][j], matrix[j][-i-1], matrix[-i-1][-j-1]

    return matrix



if __name__ == "__main__":
    # Looks like
    # 1 2 3
    # 4 5 6
    # 7 8 9
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Looks like
    # 7 4 1
    # 8 5 2
    # 9 6 3
    print(rotate(matrix))
    # [
    #   [7, 4, 1],
    #   [8, 5, 2],
    #   [9, 6, 3]
    # ]