"""
This problem was recently asked by LinkedIn:

You are given a positive integer N which represents the number of steps in a staircase.
You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.

"""

def staircase(n):
    result = [0 for x in range(n + 1)]
    result[0], result[1] = 1, 1

    for i in range(2, n + 1):
        j = 1
        while j <= 2:
            result[i] = result[i] + result[i - j]
            j = j + 1
    return result[n]


if __name__ == "__main__":
    print(staircase(4))
    # 5
    print(staircase(5))
    # 8