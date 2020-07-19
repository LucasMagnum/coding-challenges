"""
Convert to Base Two

This problem was recently asked by Apple:

Given a non-negative integer n, convert n to base 2 in string form.
Do not use any built in base 2 conversion functions like bin.

"""


def base_2(n):
    if n == 0:
        return "0"

    result = ""
    while n > 0:
        if n & 1 == 0:
            result += "0"
        else:
            result += "1"
        n >>= 1
    return result[::-1]


if __name__ == "__main__":
    print(base_2(123))
    # 1111011
