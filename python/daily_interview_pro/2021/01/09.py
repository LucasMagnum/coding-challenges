"""
Find Cycles in a Graph

This problem was recently asked by Facebook:

Given an undirected graph, determine if a cycle exists in the graph.

"""


def find_cycle(graph, visited=None):
    if visited is None:
        visited = set()

    for node, subgraph in graph.items():
        if node in visited:
            return True
        visited.add(node)

        if find_cycle(subgraph, visited):
            return True

    return False


if __name__ == "__main__":
    graph = {
        'a': {'a2':{}, 'a3':{} },
        'b': {'b2':{}},
        'c': {}
    }

    print(find_cycle(graph))
    # False
    graph['c'] = graph
    print(find_cycle(graph))
    # True
