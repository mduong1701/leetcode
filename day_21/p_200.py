import collections


def numIslands(grid):
    if not grid:
        return 0

    ROWS = len(grid)
    COLUMNS = len(grid[0])

    visited = set()
    islands = 0

    def bfs(r, c):

        q = collections.deque()
        q.append((r,c))
        
        while q:
            
            DIRECTIONS = [[1,0], [-1, 0], [0,1], [0,-1]]
            nextR, nextC = q.popleft()

            for dR, dC in DIRECTIONS:
                newRow = nextR + dR
                newColumn = nextC + dC
                if  newRow >= 0 and \
                    newRow < ROWS and \
                    newColumn >= 0 and \
                    newColumn < COLUMNS and \
                    grid[newRow][newColumn] == "1" and \
                    (newRow, newColumn) not in visited:
                        visited.add((newRow, newColumn))
                        q.append((newRow, newColumn))

    for row in range(ROWS):
        for column in range(COLUMNS):
            if grid[row][column] == "1" and (row, column) not in visited:
                bfs(row, column)
                islands += 1

    return islands