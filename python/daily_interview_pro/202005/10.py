"""
Reverse a Directed Graph

This problem was recently asked by Facebook:

Given a directed graph, reverse the directed graph so all directed edges are reversed.

Example:
Input:
A -> B, B -> C, A -> C

Output:
B-> A, C -> B, C -> A

"""

from collections import defaultdict


class Node:
    def __init__(self, value):
        self.adjacent = []
        self.value = value

    def __repr__(self):
        return self.value


def reverse_graph(graph):
    new_graph = {}

    for _, node in graph.items():
        for adjacent in node.adjacent:
            new_graph[adjacent.value] = new_graph.get(adjacent.value, [])
            new_graph[adjacent.value].append(node.value)

    for key in graph:
        graph[key].adjacent = new_graph.get(key, [])

    return graph


if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')

    a.adjacent += [b, c]
    b.adjacent += [c]

    graph = {
        a.value: a,
        b.value: b,
        c.value: c,
    }

    for key, val in reverse_graph(graph).items():
        print(key, val.adjacent)