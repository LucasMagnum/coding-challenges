"""
Permutations of numbers

This problem was recently asked by Facebook:

You are given an array of integers. Return all the permutations of this array.

> permute([1, 2, 3])
[[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]

"""


def permutations(numbers):
    if len(numbers) == 0:
        return [[]]

    first_number = numbers[0]
    reminder = numbers[1:]

    permutations_values = permutations(reminder)

    new_permutations = []
    for permutation in permutations_values:
        for index in range(len(permutation) + 1):
            new_permutations.append(
                permutation[:index] + [first_number] + permutation[index:]
            )
    return new_permutations


if __name__ == "__main__":
    permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
