"""
Phone Numbers

This problem was recently asked by AirBNB:

Given a phone number, return all valid words that can be created using that phone number.

For instance, given the phone number 364
we can construct the words ['dog', 'fog'].

"""

letters_map = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    0: []
}

valid_words = ['dog', 'fish', 'cat', 'fog']


def make_words(phone):
    digits = []

    for digit in phone:
        digits.append(int(digit))
    return make_words_helper(digits, [])


def make_words_helper(digits, letters):
    if not digits:
        word = "".join(letters)

        if word in valid_words:
            return [word]
        return []

    results = []
    chars = letters_map[digits[0]]
    for char in chars:
        results += make_words_helper(digits[1:], letters + [char])
    return results


if __name__ == "__main__":
    print(make_words('364'))