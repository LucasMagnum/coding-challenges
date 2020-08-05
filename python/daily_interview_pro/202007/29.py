"""
Minimum Number of Operations

This problem was recently asked by LinkedIn:

You are only allowed to perform 2 operations, multiply a number by 2, or subtract a number by 1.
Given a number x and a number y, find the minimum number of operations needed to go from x to y.
"""


def min_operations(x, y):
    ops = 0
    while y > x:
        if y % 2 == 0:
            y /= 2
        else:
            y += 1
        ops += 1

    ops += x - y
    return ops


if __name__ == "__main__":
    print(min_operations(6, 20))
    # (((6 - 1) * 2) * 2) = 20 : 3 operations needed only
    # print 3