from collections import deque


def orangesRotting(grid):
    fresh = 0
    time = 0
    rottenQ = deque()
    ROWS = len(grid)
    COLS = len(grid[0])

    for row in range(ROWS):
        for column in range(COLS):
            if grid[row][column] == 1:
                fresh += 1
            if grid[row][column] == 2:
                rottenQ.append([row, column])

    # 2   1   1
    # 1   1   0
    # 0   1   1

    DIRECTIONS = [[0,1], [0,-1], [1,0], [-1,0]]

    while rottenQ and fresh > 0:
        for i in range(len(rottenQ)):
            rottenR, rottenC = rottenQ.popleft()
            for dr, dc in DIRECTIONS:
                newRottenR = rottenR + dr
                newRottenC = rottenC + dc
                if  newRottenR < 0 or newRottenR == ROWS or newRottenC < 0 or newRottenC == COLS:
                    continue
                if grid[newRottenR][newRottenC] == 1:
                    grid[newRottenR][newRottenC] = 2
                    rottenQ.append([newRottenR, newRottenC])
                    fresh -= 1
        
        time += 1
    
    return time if fresh == 0 else -1

example = [[2,1,1],[1,1,0],[0,1,1]]
# example = [[2,1,1],[0,1,1],[1,0,1]]
# example = [[0,2]]
result = orangesRotting(example)
print(result)

