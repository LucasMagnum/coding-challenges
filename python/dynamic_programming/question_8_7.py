"""
    Permutations without Dups:
        Write a method to compute all permutations of a string 
        of unique characters
"""


def recursive(string):
    if len(string) == 0:
        return [""]

    first_char = string[0]
    reminder = string[1:]

    permutations = recursive(reminder)  # [b]

    new_permutations = []
    for permutation in permutations:
        for index in range(len(permutation) + 1):
            new_permutations.append(
                permutation[:index] + first_char + permutation[index:]
            )
    return new_permutations


if __name__ == "__main__":
    string = "aaaaab"
    print("Solution: ", len(recursive(string)))
