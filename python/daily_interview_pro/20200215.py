"""

Number of Ways to Climb Stairs

This problem was recently asked by LinkedIn:

You are given a positive integer N which represents the number of steps in a staircase. You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.

"""
import sys


def solution(n):
    if n <= 1:
        return 1

    return solution(n - 1) + solution(n - 2)


def solution_bottom_up(n):
    results = [0 for x in range(n + 1)]
    results[0], results[1] = 1, 1

    for i in range(2, n + 1):
        j = 1
        while j <= 2 and j <= i:
            results[i] = results[i] + results[i - j]
            j = j + 1
    return results[n]


if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
    except (IndexError, ValueError):
        n = 5

    print(f"Solution({n}) ->", solution(n))
    print(f"Solution({n}) ->", solution_bottom_up(n))