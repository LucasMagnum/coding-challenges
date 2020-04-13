"""
Circle of Chained Words

This problem was recently asked by Facebook:

Two words can be 'chained' if the last character of the first word is the same as the first character of the second word.

Given a list of words, determine if there is a way to 'chain' all the words in a circle.

Example:
Input: ['eggs', 'karat', 'apple', 'snack', 'tuna']
Output: True

"""

from collections import defaultdict

def solution(words):
    graph = defaultdict(list)
    for word in words:
        graph[word[0]].append(word)

    return dfs(graph, set(), words[0], words[0], len(words))


def dfs(graph, visited, curr, start_word, length):
    if length == 1:
        if start_word[0] == curr[-1]:
            return True
        else:
            return False
    visited.add(curr)

    for neighbor in graph[curr[-1]]:
        if neighbor not in visited:
            return dfs(graph, visited, neighbor, start_word, length - 1)

    visited.remove(curr)
    return False


if __name__ == "__main__":
    print(solution(["eggs", "karat", "apple", "snack", "tunna"]))
    print(solution(["ana", "karat", "apple", "isnack", "elisi", "tuna"]))



