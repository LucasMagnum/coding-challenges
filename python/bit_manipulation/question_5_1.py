"""
Insertion:

You are given two 32-bit numbers, N and M, and two bit positions, i and j.
Write a method to insert M into N such that M starts at bit J and ends at bit i.

You can assume that the bits j through i have enough space to fit all M. That is,
if M = 10011, you can assume that there at least 5 bits between j and i. You would
not, for example, have j = 3 and i = 2, because M could not fully fit between bit 3 and 2.

Example:

Input:  N = 10000000000 (1024), M = 10011 (19), i = 2, j = 6
Output: N = 10001001100
"""


def solution(n, m, i, j):
    if i > j or i < 0 or j >= 32:
        return 0

    # Create a mask to clear bits i through j in N.
    all_ones = ~0

    # 1s before position j, then 0s.
    left = (all_ones << (j + 1)) if j < 31 else 0

    # 1's after position i.
    right = (1 << i) - 1

    # All 1s, except for 0s between i and j.
    mask = left | right

    # Clear bits j through i then put m in there
    n_cleared = n & mask
    m_shifted = m << i

    return n_cleared | m_shifted


if __name__ == "__main__":
    n, m, i, j = 1024, 19, 2, 6
    print(
        f"Solution({bin(n)}, {bin(m)}, {i}, {j}) => 1100  ----->", solution(n, m, i, j)
    )
