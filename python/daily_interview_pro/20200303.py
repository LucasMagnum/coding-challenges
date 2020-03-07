"""
Spiral Traversal of Grid

This problem was recently asked by Amazon:

You are given a 2D array of integers. Print out the clockwise spiral traversal of the matrix.

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


def solution(grid):
    remaining = len(grid) * len(grid[0])

    current_direction = RIGHT
    current_position = (0, 0)

    while remaining > 0:
        row, column = current_position
        yield grid[row][column]
        grid[row][column] = None
        remaining -= 1

        possible_next_position = next_position(current_position, current_direction)
        if should_change_direction(
            grid, possible_next_position[0], possible_next_position[1]
        ):
            current_direction = next_direction(current_direction)
            current_position = next_position(current_position, current_direction)
        else:
            current_position = possible_next_position


def next_position(position, direction):
    if direction == RIGHT:
        return (position[0], position[1] + 1)

    if direction == DOWN:
        return (position[0] + 1, position[1])

    if direction == LEFT:
        return (position[0], position[1] - 1)

    if direction == UP:
        return (position[0] - 1, position[1])


def should_change_direction(grid, row, column):
    in_bounds_row = 0 <= row < len(grid)
    in_bounds_column = 0 <= column < len(grid[0])

    return not in_bounds_row or not in_bounds_column or grid[row][column] is None


def next_direction(direction):
    return {RIGHT: DOWN, DOWN: LEFT, LEFT: UP, UP: RIGHT}[direction]


if __name__ == "__main__":
    grid = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
    ]

    print("Solution -> ", list(solution(grid)))
