"""
Power Function

This problem was recently asked by AirBNB:

The power function calculates x raised to the nth power.
If implemented in O(n) it would simply be a for loop over n and multiply x n times.
Instead implement this power function in O(log n) time.
You can assume that n will be a non-negative integer.

"""


def pow(x, n):
    result = 1

    while n > 0:
        if n % 2 == 1:
            result = result * x
            n = n - 1

        x = x * x
        n = n / 2

    return result


if __name__ == "__main__":
    print(pow(5, 3))
