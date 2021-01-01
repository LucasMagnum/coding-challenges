"""
Making Change

This problem was recently asked by Uber:

Given a list of possible coins in cents, and an amount (in cents) n,
return the minimum number of coins needed to create the amount n.
If it is not possible to create the amount using the given coin denomination, return None.
"""


def solution(coins, n):
    min_coins = [None] * (n + 1)
    min_coins[0] = 0

    for i in range(n):
        for c in coins:
            if i + c <= n:
                if min_coins[i + c] is not None:
                    min_coins[i + c] = min(min_coins[i] + 1, min_coins[i + c])
                else:
                    min_coins[i + c] = min_coins[i] + 1
    return min_coins[-1]


if __name__ == "__main__":
    print(solution([1, 5, 10, 25], 36))
