"""
This problem was recently asked by Facebook:

Given a list of building in the form of (left, right, height),
return what the skyline should look like.

The skyline should be in the form of a list of (x-axis, height),
where x-axis is the next point where there is a change in height starting from 0,
and height is the new height starting from the x-axis.
"""
import heapq


def solution(buildings):
    tallest = []
    skyline = []

    buildings += [(x + 1, x + 1, 0) for (_, x, _) in buildings]
    buildings.sort(key=lambda x: (x[0], -x[2]))

    for l, r, h in buildings:
        # Remove shorter buildings behind current building.
        while tallest and l >= tallest[0][1]:
            heapq.heappop(tallest)

        # Add current building to heap.
        heapq.heappush(tallest, (-h, r))

        # Append to skyline if the building is not the tallest.
        if not skyline or skyline[-1][1] != -tallest[0][0]:
            skyline.append((l, -tallest[0][0]))

    return skyline


if __name__ == "__main__":
    print(solution([(2, 8, 3), (4, 6, 5)]))