"""
Find Closest Points

This problem was recently asked by LinkedIn:

Given a list of points as a tuple (x, y) and an integer k,
find the k closest points to the origin (0, 0).

"""
import heapq


def closest_points(points, k):
    pq = []

    for point in points:
        heapq.heappush(pq, (-(point[0]**2 * point[1]**2), point))

        if len(pq) > k:
            heapq.heappop(pq)

    return [x[1] for x in pq]


if __name__ == "__main__":
    print(closest_points([(0, 0), (1, 2), (-3, 4), (3, 1)], 2))
    # [(1, 2), (0, 0)]