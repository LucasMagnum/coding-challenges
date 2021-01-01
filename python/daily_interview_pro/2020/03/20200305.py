"""
Merge Overlapping Intervals

This problem was recently asked by Microsoft:

You are given an array of intervals - that is, an array of tuples (start, end). The array may not be sorted, and could contain overlapping intervals. Return another array where the overlapping intervals are merged.

For example:
[(1, 3), (5, 8), (4, 10), (20, 25)]

This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10) can be merged into (4, 10).

"""


def solution(array):
    result = []

    for start, end in sorted(array, key=lambda i: i[0]):
        if result and start <= result[-1][1]:
            prev_start, prev_end = result[-1]
            result[-1] = (prev_start, max(end, prev_end))
        else:
            result.append((start, end))

    return result


if __name__ == "__main__":
    array = [(1, 3), (2, 5), (5, 8), (4, 10), (20, 25)]

    print(f"Solution({array})", solution(array))
