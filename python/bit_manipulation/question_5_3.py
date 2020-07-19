"""
Flip Bit to Win

You have an integer and you can flip exactly one bit from 0 to a 1.
Write code to find the length of the longest sequence of 1s you could
create.

EXAMPLE

Input: 1775  (or: 11011101111)
Output: 8

"""


def flip_bit(number):
    # Currently has the longest sequence
    if ~number == 0:
        return number.bit_length()

    current = 0
    previous = 0
    max_length = 1

    while number != 0:
        if (number & 1) == 1:
            current += 1
        elif (number & 1) == 0:
            # Update to 0 if next bit is 0 or current if next bit is 1
            previous = 0 if number & 2 == 0 else current
            current = 0
        max_length = max([previous + current + 1, max_length])
        number >>= 1

    return max_length


if __name__ == "__main__":
    print(flip_bit(1775))
