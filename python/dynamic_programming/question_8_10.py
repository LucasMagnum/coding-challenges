"""
    Paint Fill:
        Implement the paint fill function that one might see on many
        editing programs.
        That is, given a screen (represented by two-dimensional array of colors),
        a point, and a new color, fill the surrounding area until the color changes
        from the original color.
"""


def paint_fill(screen, point, color):
    row, column = point

    if screen[row][column] == color:
        return False

    def _paint_fill(row, column, original_color):
        if row < 0 or row >= len(screen) or column < 0 or column >= len(screen[0]):
            return False

        if screen[row][column] == original_color:
            screen[row][column] = color

            _paint_fill(row - 1, column, original_color)  # Up
            _paint_fill(row + 1, column, original_color)  # Down
            _paint_fill(row, column - 1, original_color)  # Left
            _paint_fill(row, column + 1, original_color)  # Right

        return True

    _paint_fill(row, column, screen[row][column])
    return screen


if __name__ == "__main__":
    screen = [
        [0, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    print("Solution: ", paint_fill(screen, (1, 2), 254))
