class Solution:
    def minPathSum(self, grid):
        ROWS = len(grid)
        COLS = len(grid[0])

        for i in range(COLS - 2, -1, -1):
            grid[-1][i] += grid[-1][i + 1]

        for j in range(ROWS - 2, -1, -1):
            grid[j][-1] += grid[j + 1][-1]

        for row in range(ROWS - 2, -1, -1):
            for col in range(COLS - 2, -1, -1):
                grid[row][col] += min(grid[row + 1][col], grid[row][col + 1])

        return grid[0][0]