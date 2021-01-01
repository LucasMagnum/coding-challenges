"""
Subarray With Target Sum

This problem was recently asked by Amazon:

You are given an array of integers, and an integer K.
Return the subarray which sums to K. You can assume that a solution will always exist.

"""


def solution(array, k):
    previous = dict()
    total = 0

    previous[0] = -1

    for last_idx, item in enumerate(array):
        total += item
        previous[total] = last_idx

        first_idx = previous.get(total - k)
        if first_idx is not None:
            return array[first_idx + 1 : last_idx + 1]

    return None


if __name__ == "__main__":
    array = [1, 3, 3, 3, 3, 1, 2, 5, 7, 2]
    k = 14
    print(solution(array, k))
