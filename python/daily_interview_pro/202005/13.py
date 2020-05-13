"""
Consecutive Ones

This problem was recently asked by Microsoft:

Return the longest run of 1s for a given integer n's binary representation.

Example:

Input: 242
Output: 4
242 in binary is 0b11110010, so the longest run of 1 is 4.

"""


def solution(n):
    longest = 0
    run = 0
    bitmask = 1

    while n != 0:
        if n & bitmask == 0:
            longest = max(longest, run)
            run = 0
        else:
            run += 1

        n = n >> 1

    return max(longest, run)



if __name__ == "__main__":
    print(solution(242))