def pacific(heights):
    ROWS = len(heights)
    COLS = len(heights[0])

    pacific = set()
    atlantic = set()

    def dfs(row, column, ocean, prevHeight):
        if (
            row < 0 or
            row == ROWS or
            column < 0 or
            column == COLS or
            (row, column) in ocean or
            heights[row][column] < prevHeight
        ):
            return
        ocean.add((row, column))
        dfs(row + 1, column, ocean, heights[row][column])
        dfs(row - 1, column, ocean, heights[row][column])
        dfs(row, column + 1, ocean, heights[row][column])
        dfs(row, column - 1, ocean, heights[row][column])

    for c in range(COLS):
        dfs(0, c, pacific, heights[0][c])
        dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

    for r in range(ROWS):
        dfs(r, 0, pacific, heights[r][0])
        dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

    result = []

    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in pacific and (r, c) in atlantic:
                result.append([r, c])

    return result