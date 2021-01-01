"""
Connected colors in a grid

This problem was recently asked by Uber:

Find the maximum number of connected colors in a grid.

"""


def max_connected_colors(grid):
    max_n = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            # max_n = max(max_n, self.dfs(x, y, {}))
            max_n = max(max_n, dfs(grid, x, y, {}))
    return max_n


def dfs(grid, x, y, visited):
    key = str(x) + ',' + str(y)
    if key in visited:
        return 0
    visited[key] = True
    result = 1
    for neighbor in neighbors(grid, x, y):
        result += dfs(grid, neighbor[0], neighbor[1], visited)
    return result


def dfs_interative(grid, x, y, visited):
    stack = [(x, y)]
    result = 0
    while len(stack) > 0:
        (x, y) = stack.pop()
        key = str(x) + ', ' + str(y)
        if key in visited:
            continue
        visited[key] = True

        result += 1
        for neighbor in neighbors(grid, x, y):
            stack.append(neighbor)
    return result


def neighbors(grid, x, y):
    POSITIONS = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    n = []
    for pos in POSITIONS:
        if color_at(grid, x + pos[0], y + pos[1]) == color_at(grid, x, y):
            n.append((x + pos[0], y + pos[1]))
    return n


def color_at(grid, x, y):
    if x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid):
        return grid[y][x]
    return -1



if __name__ == "__main__":
    grid = [[1, 0, 0, 1],
            [1, 1, 1, 1],
            [0, 1, 0, 0]]

    print(max_connected_colors(grid))
    # 7