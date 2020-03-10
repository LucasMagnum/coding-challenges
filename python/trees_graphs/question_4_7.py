"""
Build Order

You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where
the second project is dependent on the first project).

All project's dependencies must be built before the project is. Find a build order that will allow
the projects to be built. If there is no valid build order return an error.

Ex:

Input
    projects: a, b, c, d, e, f
    dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)

Output
    f, e, a, b, d, c

"""


class Graph:
    def __init__(self):
        self.nodes = []
        self.mapping = {}

    def add_edge(self, start_name, end_name):
        start = self.get_or_create_node(start_name)
        end = self.get_or_create_node(end_name)

        start.add_neighbor(end)

    def get_or_create_node(self, name):
        if name not in self.mapping:
            node = Project(name)
            self.nodes.append(node)
            self.mapping[name] = node
        return self.mapping[name]

    def __str__(self):
        return f"{self.nodes}"


class Project:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.mapping = {}
        self.dependencies = 0
        self.state = None

    def add_neighbor(self, node):
        if node.name not in self.mapping:
            self.children.append(node)
            self.mapping[node.name] = node
            node.dependencies += 1

    def __repr__(self):
        return f"<Project: {self.name}>"


def solution(projects, dependencies):
    graph = build_graph(projects, dependencies)
    return order_projects(graph.nodes)


def dfs_solution(projects, dependencies):
    graph = build_graph(projects, dependencies)
    return order_projects_dfs(graph.nodes)


def build_graph(projects, dependencies):
    graph = Graph()

    for first, second in dependencies:
        graph.add_edge(first, second)

    for project in projects:
        graph.get_or_create_node(project)

    return graph


def order_projects(projects):
    order = [None] * len(projects)

    end_of_list = add_non_dependent(order, projects, 0)
    to_be_processed = 0

    while to_be_processed < len(order):
        current = order[to_be_processed]

        if current is None:
            return

        for child in current.children:
            child.dependencies -= 1

        end_of_list = add_non_dependent(order, current.children, end_of_list)
        to_be_processed += 1

    return order


def add_non_dependent(order, projects, offset):
    for project in projects:
        if project.dependencies == 0:
            order[offset] = project
            offset += 1
    return offset


def order_projects_dfs(projects):
    stack = []

    for project in projects:
        # Project in empty state
        if project.state is None:
            if not dfs(project, stack):
                return

    return stack


def dfs(project, stack):
    # Cycle found
    if project.state == "visiting":
        return False

    if project.state is None:
        project.state = "visiting"

        for child in project.children:
            if not dfs(child, stack):
                return False

        project.state = "complete"
        stack.append(project)

    return True


if __name__ == "__main__":
    projects = ["a", "b", "c", "d", "e", "f"]
    dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]

    print(solution(projects, dependencies))
    print(dfs_solution(projects, dependencies))