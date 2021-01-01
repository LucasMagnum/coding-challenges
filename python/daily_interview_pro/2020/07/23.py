"""
Convert to Hexadecimal

This problem was recently asked by Amazon:

Given a non-negative integer n, convert the integer to hexadecimal and return the result as a string.
Hexadecimal is a base 16 representation of a number, where the digits are 0123456789ABCDEF.
Do not use any builtin base conversion functions like hex.
"""


def to_hex(n):
    if n == 0:
        return '0'

    digits = '0123456789ABCDEF'
    result = ''

    while n > 0:
        result += digits[n % 16]
        n //= 16

    return result[::-1]


if __name__ == "__main__":
    print(to_hex(123))
    # 7B