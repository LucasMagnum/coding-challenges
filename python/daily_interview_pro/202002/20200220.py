"""
Word Search

This problem was recently asked by Amazon

You are given a 2D array of characters, and a target string. Return whether or not the word target word exists in the matrix. Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix.

Example:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

Given this matrix, and the target word FOAM, you should return true, as it can be found going up-to-down in the first column.

"""


def word_search(matrix, word):
    for r, row in enumerate(matrix):
        for c, val in enumerate(row):
            if check_word_right(matrix, r, c, word):
                return True

            if check_word_down(matrix, r, c, word):
                return True
    return False


def check_word_right(matrix, r, c, word):
    word_len = len(word)
    row_len = len(matrix[0])

    if word_len != row_len - c:
        return False

    for c1, c2 in zip(word, (matrix[r][i] for i in range(c, row_len))):
        if c1 != c2:
            return False
    return True


def check_word_down(matrix, r, c, word):
    word_len = len(word)
    col_len = len(matrix)

    if word_len != col_len - r:
        return False

    for c1, c2 in zip(word, (matrix[i][c] for i in range(r, col_len))):
        if c1 != c2:
            return False
    return True


if __name__ == "__main__":

    matrix = [
        ["F", "A", "C", "I"],
        ["O", "B", "Q", "P"],
        ["A", "N", "O", "B"],
        ["M", "A", "S", "S"],
    ]

    print(word_search(matrix, "FOAM"))
