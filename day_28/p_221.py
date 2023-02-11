def maximalSquare(matrix):
    ROWS = len(matrix)
    COLUMNS =len(matrix[0])
    cache = {}

    def dfs(row, column):
        if row >= ROWS or column >= COLUMNS:
            return 0

        if (row, column) not in cache:

            down = dfs(row + 1, column)
            right = dfs(row, column + 1)
            diag = dfs(row + 1, column + 1)

            cache[(row, column)] = 0

            if matrix[row][column] == "1":
                cache[(row, column)] = 1 + min(down, right, diag)

        return cache[(row, column)]