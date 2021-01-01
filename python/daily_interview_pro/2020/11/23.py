"""
Staying on a Chess Board

 This problem was recently asked by Google:

A chess board is an 8x8 grid.
Given a knight at any position (x, y) and a number of moves k,
we want to figure out after k random moves by a knight, the probability
that the knight will still be on the chessboard.
Once the knight leaves the board it cannot move again and will be considered off the board.
"""

def is_knight_on_board(x, y, k, cache={}):
    if (x, y, k) in cache:
        return cache[(x, y, k)]
    if not (0 <= x <= 7 and 0 <= y <= 7):
        return 0
    if k == 0:
        return 1

    moves = valid_moves(x, y)
    move_probs = [is_knight_on_board(x, y, k - 1) / float(len(moves))
                  for x, y in moves]
    cache[(x, y, k)] = sum(move_probs)
    return cache[(x, y, k)]

def valid_moves(x, y):
    return [
        ((x + 1), (y + 2)),
        ((x - 1), (y + 2)),
        ((x + 1), (y - 2)),
        ((x - 1), (y - 2)),
        ((x + 2), (y + 1)),
        ((x - 2), (y + 1)),
        ((x + 2), (y - 1)),
        ((x - 2), (y - 1)),
    ]


if __name__ == "__main__":
    print(is_knight_on_board(0, 0, 1))
    # 0.25