""" 
    Coins:
        Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and 
        pennies (1 cent), write code to calculate the number of ways of representing n cents.
""" 
import sys


def make_change(amount, denoms, index, cache=None):
    if cache is None: cache = {}
    if index >= len(denoms) - 1: return 1  # last denom
    if cache.get((amount, index)): return cache[(amount, index)] # cached

    denomination_amount = denoms[index]
    ways = 0

    k = 0
    while (k * denomination_amount <= amount):
        remaining = amount - k * denomination_amount
        ways += make_change(remaining, denoms, index  + 1)
        k += 1

    cache[(amount, index)] = ways
    return ways


if __name__ == "__main__":
    try:
        amount = int(sys.argv[1])
    except IndexError:
        amount = 5

    denoms = [25, 10, 5, 1]
    print("Solution: ", make_change(amount, denoms, 0))