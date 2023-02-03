def numIslands(grid):

    ROWS = len(grid)
    COLUMNS = len(grid[0])

    visited = set()
    islands = 0

    