"""
Reverse Integer

This problem was recently asked by Amazon:

Given an integer, reverse the digits. Do not convert the integer into a string and reverse it.

"""


def reverse_integer(num):
    result = 0
    negative = 1

    if num < 0:
        negative = -1
        num *= -1

    while num > 0:
        result = result * 10 + num % 10
        num //= 10

    return negative * result


if __name__ == "__main__":
    print(reverse_integer(135))
    # 531

    print(reverse_integer(-321))
    # -123