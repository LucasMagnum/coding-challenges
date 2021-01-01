"""
Sum of squares

This problem was recently asked by Facebook:

Given a number n, find the least number of squares needed to sum up to the number.

"""


def square_sum(n):
    squares = []

    # Find all squares less than n
    i = 1
    while i*i <= n:
        squares.append(i*i)
        i += 1

    # Find min possible sum up to squares for all numbers
    min_sums = [n] * (n + 1)
    min_sums[0] = 0

    for idx in range(len(min_sums)):
        for s in squares:
            if idx + s < len(min_sums):
                min_sums[idx + s] = min(min_sums[idx + s], min_sums[idx] + 1)

    return min_sums[-1]


if __name__ == "__main__":
    print(square_sum(99))
    # Min sum is 3*3 + 2*2
    # 2