"""
    Eight Queens:
         Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all
diagonals, not just the two that bisect the board. 
"""
import copy

board_size = 8


def place_queens(row, columns, results):
    if row == board_size:
        results.append(columns)
    else:
        for column in range(board_size):
            if check_valid(columns, row, column):
                columns[row] = column
                place_queens(row + 1, columns, results)


def check_valid(columns, row, column):
    current_row = 0

    while current_row < row:
        current_column = columns[current_row]

        # Check if current column and current row invalidates 
        # row and column
        if column == current_column:
            return False
        
        column_distance = abs(current_column - column)
        row_distance = row - current_row

        if column_distance == row_distance:
            return False

        current_row += 1
    return True    


if __name__ == "__main__":
    results = []
    place_queens(0, {}, results)
    print("Solution: ", results, len(results))


"""
[
    [0, 0, 0, 0, 0, 0, 0, X],
    [0, 0, 0, X, 0, 0, 0, 0],
    [X, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, X, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, X, 0, 0],
    [0, X, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, X, 0],
    [0, 0, 0, 0, X, 0, 0, 0],

]
"""
