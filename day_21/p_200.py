import collections


def numIslands(grid):
    if not grid:
        return 0

    ROWS = len(grid)
    COLUMNS = len(grid[0])

    q = collections.deque()
    visited = set()
    islands = 0

    def bfs(r, c):
        pass

    for row in range(ROWS):
        for column in range(COLUMNS):
            if grid[row][column] == "1" and (row, column) not in visited:
                bfs(row, column)
                islands += 1

    return islands