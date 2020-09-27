"""
Common Characters

This problem was recently asked by Apple:

Given a list of strings, find the list of characters that appear in all strings.
"""


def common_characters(strings):
    set_of_letters = set(strings[0])

    result = None

    for string in strings[1:]:
        result = set_of_letters & set(string)

    return result
§

if __name__ == "__main__":
    print(common_characters(['google', 'facebook', 'youtube']))
    # ['e', 'o']