"""
Concatenated Words

This problem was recently asked by Twitter:

Find all words that are concatenations of a list.

Input:
["tech", "lead", "techlead", "cat", "cats", "dog", "catsdog"]

Output:
['techlead', 'catsdog']

"""


def solution(words):
    word_dict = set(words)
    cache = {}
    return [word for word in words if can_form_word(word, word_dict, cache)]


def can_form_word(word, word_dict, cache, depth=0):
    if word in cache:
        return cache[word]

    for index in range(1, len(word)):
        if (
            word[index:] in word_dict or
            can_form_word(word[index:], word_dict, cache, depth + 1)
        ):
            if word[:index] in word_dict:
                cache[word] = True
                return True
    cache[word] = False
    return False


if __name__ == "__main__":
    words = ["tech", "lead", "techlead", "cat", "cats", "dog", "catsdog"]
    print(solution(words))