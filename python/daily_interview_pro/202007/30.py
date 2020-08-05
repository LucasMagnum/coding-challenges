"""
Shortest Distance to Character

This problem was recently asked by Uber:

Given a string s and a character c, find the distance for all characters in the string to the character c
in the string s. You can assume that the character c will appear at least once in the string.


"""
def shortest_dist(s, c):
    result = [float('inf')] * len(s)

    c_idx = float('inf')
    for idx, ch in enumerate(s):
        if ch == c:
            c_idx = idx
            result[idx] = 0
        elif c_idx != float('inf'):
            result[idx] = idx - c_idx

    c_idx = float('inf')
    for idx, ch in reversed(list(enumerate(s))):
        if ch == c:
            c_idx = idx
            result[idx] = 0
        elif c_idx != float('inf'):
            result[idx] = min(result[idx], c_idx - idx)

    return result


if __name__ == "__main__":
    print(shortest_dist('helloworld', 'l'))
    # [2, 1, 0, 0, 1, 2, 2, 1, 0, 1]
