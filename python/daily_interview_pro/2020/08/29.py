"""
Closest points to origin

This problem was recently asked by Google:

Given a list of points and a number k, find the k closest points to the origin.

"""

import heapq


def solution_sort(points, k):
    points = sorted(points, key = lambda x: calculate_distance(x))
    return points[:k]


def solution_heap(points, k):
    # ( distance, object )
    data = []
    for p in points:
        data.append((calculate_distance(p), p))
    heapq.heapify(data)

    result = []
    for i in range(k):
        result.append(heapq.heappop(data)[1])
    return result


def calculate_distance(p):
    return p[0]*p[0] + p[1]*p[1]


if __name__ == "__main__":
    print(solution_sort([[1, 1], [3, 3], [2, 2], [4, 4], [-1, -1]], 3))
    # [[-1, -1], [1, 1], [2, 2]]
    print(solution_heap([[1, 1], [3, 3], [2, 2], [4, 4], [-1, -1]], 3))
    # [[-1, -1], [1, 1], [2, 2]]