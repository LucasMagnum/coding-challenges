"""
    Permutations with duplicates:
        Write a method to compute all permutations of a string 
        whose characters are not necessarily unique. The list of permutations
        should not have duplicates.
"""


def recursive(string):
    result = []
    frequency = get_characters_frequency(string)
    build_permutations(frequency, "", len(string), result)
    return result


def get_characters_frequency(string):
    counter = {}
    for character in string:
        counter[character] = counter.get(character, 0) + 1
    return counter


def build_permutations(frequency, prefix, remaining, result):
    # Base case. Permutation has been completed
    if remaining == 0:
        result.append(prefix)
        return

    # Try remaining letters for next char and generate remaining permutations
    for character, count in frequency.items():
        if count > 0:
            frequency[character] -= 1
            build_permutations(frequency, prefix + character, remaining - 1, result)
            frequency[character] = count


if __name__ == "__main__":
    string = "abcd"
    print("Solution: ", recursive(string))
