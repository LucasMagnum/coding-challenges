"""
    Recursive Multiply:
        Write a recursive function to multiply two positive integers without
        using the * operator. You can use addition, substraction, and bit shifting, but
        you should minimize the number of those operations.
"""


def brute_force(a, b):
    if a == 0 or b == 0:
        return 0

    if b == 1:
        return a

    return a + brute_force(a, b - 1)


def doubling_sum(a, b):
    smaller, bigger = (a, b) if a < b else (b, a)

    def _multiply(smaller, bigger):
        if smaller == 0:
            return 0
        if smaller == 1:
            return bigger

        smaller_divided = smaller >> 1
        left_side = _multiply(smaller_divided, bigger)
        right_side = left_side

        if smaller % 2 == 1:
            right_side = _multiply(smaller - smaller_divided, bigger)

        return left_side + right_side

    return _multiply(smaller, bigger)


def doubling_sum_cached(a, b):
    smaller, bigger = (a, b) if a < b else (b, a)

    def _multiply(smaller, bigger, cache=None):
        if cache is None:
            cache = {}

        if smaller == 0:
            return 0
        if smaller == 1:
            return bigger

        if cache.get(smaller):
            return cache[smaller]

        smaller_divided = smaller >> 1
        left_side = _multiply(smaller_divided, bigger, cache)
        right_side = left_side

        if smaller % 2 == 1:
            right_side = _multiply(smaller - smaller_divided, bigger, cache)

        sides_sum = left_side + right_side
        cache[smaller] = sides_sum
        return sides_sum

    return _multiply(smaller, bigger)


if __name__ == "__main__":
    a, b = (1604, 800)  # 800 iterations
    print("Solution: ", brute_force(a, b))

    a, b = (1604, 800)  # 26 iterations
    print("Solution doubling sum: ", doubling_sum(a, b))

    a, b = (1604, 800)  # 18 iterations
    print("Solution doubling sum cached: ", doubling_sum_cached(a, b))
