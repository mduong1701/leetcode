def maximalSquare(matrix):
    ROWS = len(matrix)
    COLUMNS =len(matrix[0])
    cache = {}

    def dfs(row, column):
        if row >= ROWS or column >= COLUMNS:
            return 0

        