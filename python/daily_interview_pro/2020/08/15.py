"""
Number of 1 bits

This problem was recently asked by Google:

Given an integer, find the number of 1 bits it has.

"""

def one_bits(num):
    count = 0

    while num > 0:
        if num & 1 == 1:
            count += 1
        num >>= 1

    return count


print(one_bits(23))
# 4
# 23 = 0b10111


