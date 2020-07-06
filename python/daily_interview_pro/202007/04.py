"""
Squareroot

This problem was recently asked by Google:

Given a positive integer, find the square root of the integer without using any built
in square root or power functions (math.sqrt or the ** operator).
Give accuracy up to 3 decimal points.
"""


def sqrt(x):
    low = 0
    high = x

    while (high - low) > 0.001:
        mid = (low + high) / 2

        square = mid * mid

        if abs(square - x) < 0.0001:
            return mid

        elif x < square:
            high = mid

        else:
            low = mid

    return round((high + low) / 2, 3)


if __name__ == "__main__":
    print(sqrt(5))
    # 2.236
