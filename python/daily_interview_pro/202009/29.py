"""
H-Index

This problem was recently asked by Amazon:

The h-index is a metric that attempts to measure the productivity and citation impact of the publication of a scholar. The definition of the h-index is if a scholar has at least h of their papers cited h times.

Given a list of publications of the number of citations a scholar has, find their h-index.

Example:
    Input: [3, 5, 0, 1, 3]
    Output: 3

Explanation:
There are 3 publications with 3 or more citations, hence the h-index is 3.

"""

def solution(publications):
    n = len(publications)
    citations = [0] * (n + 1)

    for pub in publications:
        if pub < n:
            citations[pub] += 1
        else:
            citations[n] += 1

    total = 0
    i = n
    while i >= 0:
        total += citations[i]
        if total >= i:
            return i
        i -= 1

    return i

if __name__ == "__main__":
    print(solution([5, 3, 3, 1, 0]))
    # 3