"""
This problem was recently asked by Amazon:

You are given a 2D array of integers.
Print out the clockwise spiral traversal of the matrix.

Example:

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

The clockwise spiral traversal of this array is:

1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12

"""

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


def next_direction(direction):
    return {
        RIGHT: DOWN,
        DOWN: LEFT,
        LEFT: UP,
        UP: RIGHT
    }[direction]

def next_position(position, direction):
    row, column = position

    if direction == RIGHT:
        return (row, column + 1)
    elif direction == DOWN:
        return (row + 1, column)
    elif direction == LEFT:
        return (row, column - 1)
    elif direction == UP:
        return (row - 1, column)


def should_change_direction(M, r, c):
    in_bounds_r = 0 <= r < len(M)
    in_bounds_c = 0 <= c < len(M[0])
    return (not in_bounds_r or
            not in_bounds_c or
            M[r][c] is None)


def matrix_spiral_print(M):
    remaining = len(M) * len(M[0])
    current_direction = RIGHT
    current_position = (0, 0)

    while remaining > 0:
        r, c = current_position
        print(M[r][c], end=", ")
        M[r][c] = None
        remaining -= 1

        possible_next_position = next_position(current_position, current_direction)
        if should_change_direction(M, possible_next_position[0], possible_next_position[1]):
            current_direction = next_direction(current_direction)
            current_position = next_position(current_position, current_direction)
        else:
            current_position = possible_next_position


if __name__ == "__main__":
    grid = [[1,  2,  3,  4,  5],
            [6,  7,  8,  9,  10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]]

    matrix_spiral_print(grid)
    # 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12