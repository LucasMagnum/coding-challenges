"""
Staying on a Chess Board

This problem was recently asked by Google:

A chess board is an 8x8 grid. Given a knight at any position (x, y) and a number of moves k,
we want to figure out after k random moves by a knight,
the probability that the knight will still be on the chessboard.

Once the knight leaves the board it cannot move again and will be considered off the board.

"""

def solution(x, y, moves, cache={}):
    if (x, y, moves) in cache:
        return cache[(x, y, moves)]

    if not (0 <= x <= 7 and 0 <= y <= 7):
        return 0

    if moves == 0:
        return 1

    valid_moves = get_valid_moves(x, y)
    move_probs = [
        solution(x, y, moves - 1) / float(len(valid_moves)) for x, y in valid_moves
    ]
    cache[(x, y, moves)] = sum(move_probs)
    return cache[(x, y, moves)]

def get_valid_moves(x, y):
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
    print(solution(3, 3, 1))