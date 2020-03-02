"""
Edit Distance

This problem was recently asked by AirBNB:

Given two strings, determine the edit distance between them. The edit distance is defined as the minimum number of edits (insertion, deletion, or substitution) needed to change one string to the other.

For example, "biting" and "sitting" have an edit distance of 2 (substitute b for s, and insert a t).

"""


def solution(first, second):
    if len(first) == 0 or len(second) == 0:
        return max(len(first), len(second))

    return min(
        solution(first[1:], second) + 1,
        solution(first, second[1:]) + 1,
        solution(first[1:], second[1:])
        if first[0] == second[0]
        else solution(first[1:], second[1:]) + 1,
    )


def cached_solution(first, second):
    x = len(first) + 1
    y = len(second) + 1

    A = [[-1 for i in range(x)] for j in range(y)]
    for i in range(x):
        A[0][i] = i

    for j in range(y):
        A[j][0] = j

    for i in range(1, y):
        for j in range(1, x):
            if first[j - 1] == second[i - 1]:
                A[i][j] = A[i - 1][j - 1]
            else:
                A[i][j] = min(A[i - 1][j] + 1, A[i][j - 1] + 1, A[i - 1][j - 1] + 1)
    return A[y - 1][x - 1]


if __name__ == "__main__":
    first, second = "lucasmagnum", "lopesoliveira"
    print(f"Solution({first}, {second}) ->", cached_solution(first, second))
