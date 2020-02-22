"""
Route between nodes:
    Given a directed graph and two nodes (S and E), design an algorithm to find out whether there is 
    a route from S to E.
"""
from collections import deque


def find_connection_bfs(graph, start, end):
    if start == end:
        return True

    queue = deque()
    queue.append(start)
    seen = set()

    while queue:
        node = queue.popleft()
        for adjacent_node in graph[node]:
            if adjacent_node == end:
                return True

            if adjacent_node:
                queue.append(adjacent_node)

        seen.add(node)

    return False


def find_connection_dfs(graph, start, end, seen=None):
    if seen is None:
        seen = set()

    if start == end:
        return True

    seen.add(start)

    for node in graph[start]:
        if node in seen:
            continue

        if find_connection_dfs(graph, node, end, seen):
            return True

    return False


if __name__ == "__main__":
    graph = [[1, 4, 5], [3, 4], [1], [2, 4], [], []]
    first_node, second_node = 0, 2

    print(
        f"find_connection_bfs({first_node}, {second_node}) -> ",
        find_connection_bfs(graph, first_node, second_node),
    )
    print(
        f"find_connection_dfs({first_node}, {second_node}) -> ",
        find_connection_dfs(graph, first_node, second_node),
    )
