"""
Find the Number of Islands

This problem was recently asked by LinkedIn:

Given a 2-dimensional grid consisting of 1's (land blocks) and 0's (water blocks), 
count the number of islands present in the grid. The definition of an island is as follows:

1.) Must be surrounded by water blocks.
2.) Consists of land blocks (1's) connected to adjacent land blocks (either vertically or horizontally).
Assume all edges outside of the grid are water.

Example:
Input: 
10001
11000
10110
00000

Output: 3

"""

def solution(grid):
    if not grid or not grid[0]:
        return 0
    rows, columns = len(grid), len(grid[0])
    count = 0
    for i in range(rows):
        for j in range(columns):
            # if we find a land block, run dfs
            # starting at this block.
            if grid[i][j] == 1:
                bfs(grid, i, j)
                count += 1
                print(grid)
    return count


def bfs(grid, currRow, currCol):
    queue = []
    queue.append((currRow, currCol))
    # mark current vertex as visited
    grid[currRow][currCol] = 2

    while queue:
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        currRow, currCol = queue.pop()
        for d in directions:
            nextRow, nextCol = currRow + d[0], currCol + d[1]
            if inRange(grid, nextRow, nextCol) and grid[nextRow][nextCol] == 1:
                queue.append((nextRow, nextCol))
                # mark next vertex and column as visited so
                # we don't double count
                grid[nextRow][nextCol] = 2


def dfs(grid, currRow, currCol):
    grid[currRow][currCol] = 2
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for d in directions:
        nextRow, nextCol = currRow + d[0], currCol + d[1]
        if inRange(grid, nextRow, nextCol) and grid[nextRow][nextCol] == 1:
            dfs(grid, nextRow, nextCol)


def inRange(grid, r, c):
    numRow, numCol = len(grid), len(grid[0])
    if r < 0 or c < 0 or r >= numRow or c >= numCol:
        return False
    return True

if __name__ == "__main__":
    grid = [[1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0]]
    print(solution(grid))