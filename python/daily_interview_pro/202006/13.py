"""
This problem was recently asked by Apple:

Given a list of points, an interger k, and a point p, find the k closest points to p.

"""
import heapq


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    # Doesn't matter which value is greater, first tuple value should
    # determine the ordering.
    def __gt__(self, p):
        return True


def point_dist_squared(p1, p2):
    return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2


def closest_points(points, k, p):
    closest = []

    for point in points:
        dist = point_dist_squared(p, point)
        heapq.heappush(closest, (-dist, point))
        if len(closest) > k:
            heapq.heappop(closest)

    return [point for _, point in closest]


if __name__ == "__main__":
    points = [
        Point(0, 0),
        Point(1, 1),
        Point(2, 2),
        Point(3, 3),
    ]
    print(closest_points(points, 2, Point(0, 2)))
    # [(0, 0), (1, 1)]
