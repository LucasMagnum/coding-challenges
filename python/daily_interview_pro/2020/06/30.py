"""
Swap bits

This problem was recently asked by Twitter:

Given a 32-bit integer, swap the 1st and 2nd bit, 3rd and 4th bit, up til the 31st and 32nd bit.

"""

MASK_EVEN = 0b10101010101010101010101010101010
MASK_ODD = 0b01010101010101010101010101010101


def solution(number):
    return ((number & MASK_EVEN) >> 1) | ((number & MASK_ODD) << 1)


if __name__ == "__main__":
    print(bin(solution(0b10101010101010101010101010101010)))
