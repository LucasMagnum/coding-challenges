"""
Zero Matrix: 
    Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
    column are set to 0
"""
from typing import List


def solution(matrix: List[List[int]]) -> List[List[int]]:
    marked_rows = set()
    marked_columns = set()

    for row_index, row in enumerate(matrix):
        for column_index, column in enumerate(row):
            if column == 0:
                marked_rows.add(row_index)
                marked_columns.add(column_index)

    for row_index in marked_rows:
        matrix[row_index] = [0 for _ in range(len(matrix[row_index]))]

    for column_index in marked_columns:
        for row_index, _ in enumerate(matrix):
            matrix[row_index][column_index] = 0

    return matrix


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4, 0], [6, 7, 8, 9, 2], [3, 4, 0, 6, 7], [1, 5, 3, 2, 1]]

    print("Solution: ", solution(matrix))
