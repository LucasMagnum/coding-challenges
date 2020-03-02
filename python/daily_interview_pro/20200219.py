"""
Find Cycles in a Graph

This problem was recently asked by Facebook:
Given an undirected graph, determine if a cycle exists in the graph.

Can you solve this in linear time, linear space?
"""


def solution(graph):
    visited = {}

    for vertex, edges in graph.items():
        if vertex not in visited:
            if find(edges, vertex, visited):
                return True
    return False


def find(graph, vertex, visited):
    if vertex in visited:
        return True

    visited[vertex] = True

    for edge, connections in graph.items():
        if find(connections, edge, visited):
            return True
    return False


if __name__ == "__main__":
    graph = {"a": {"a2": {}, "a3": {}, "a4": {}}, "b": {"b2": {}, "b3": {}}, "c": {}}

    print(f"Solution({graph}) ->", solution(graph))
    graph["c"] = graph
    print(f"Solution({graph}) ->", solution(graph))
