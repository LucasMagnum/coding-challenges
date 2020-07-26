"""
Common Characters

This problem was recently asked by Apple:

Given a list of strings, find the list of characters that appear in all strings.

"""

def common_characters(strs):
    if not strs:
        return []

    matches = set(strs[0])

    for string in strs:
        intersection = set()
        for character in string:
            if character in matches:
                intersection.add(character)
        matches = intersection

    return list(matches)


if __name__ == "__main__":
    print(common_characters(['google', 'facebook', 'youtube']))
    # ['e', 'o']