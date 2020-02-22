"""
Missing Number:
    An array A contains all the integers from 0 to N, except for one number which is missing.
    In this problem, we cannot access an entire integer in A with a single operation. The elements
    of A are represented in binary, and the only operation we can use to access them is "fetch 
    the jth bit of A[i]", which takes constant time. Write code to find the missing integer.

    Can you do it in O(n) time.
"""


def solution(array, column):
    # Fixed value here for this case
    if column >= 32:
        return 0

    one_bits = []
    zero_bits = []

    for item in array:
        if (item >> column) & 1 == 0:
            zero_bits.append(item)
        else:
            one_bits.append(item)

    if len(zero_bits) <= len(one_bits):
        v = solution(zero_bits, column + 1)
        return (v << 1) | 0
    else:
        v = solution(one_bits, column + 1)
        return (v << 1) | 1


if __name__ == "__main__":
    array = [x for x in range(0, 100) if x != 48]
    print("Solution: ", solution(array, 0))
