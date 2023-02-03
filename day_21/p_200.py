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

        DIRECTIONS = [[1,0], [-1, 0], [0,1], [0,-1]]
        
        for dR, dC in DIRECTIONS:
            newRow = r + dR
            newColumn = c + dC
            if  newRow >= 0 and \
                newRow < ROWS and \
                newColumn >= 0 and \
                newColumn < COLUMNS and \
                grid[newRow][newColumn] == "1" and \
                (newRow, newColumn) not in visited:
                    visited.add((newRow, newColumn))
                    q.popleft()

    for row in range(ROWS):
        for column in range(COLUMNS):
            if grid[row][column] == "1" and (row, column) not in visited:
                bfs(row, column)
                islands += 1

    return islands