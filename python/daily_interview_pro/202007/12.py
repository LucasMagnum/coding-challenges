"""
Number of Connected Components

This problem was recently asked by Apple:

Given a list of undirected edges which represents a graph, find out the number of connected components.

"""

from collections import defaultdict


def num_connected_components(edges):
    if not edges:
        return 0

    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    not_visited = set(graph.keys())
    connected_components = 0

    while not_visited:
        stack = [next(iter(not_visited))]
        while stack:
            node = stack.pop()
            if node in not_visited:
                not_visited.remove(node)
                for adjacent in graph[node]:
                    stack.append(adjacent)

        connected_components += 1
    return connected_components


if __name__ == "__main__":
    print(num_connected_components([(1, 2), (2, 3), (4, 1), (5, 6)]))
    # 2
