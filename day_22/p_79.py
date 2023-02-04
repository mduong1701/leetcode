def exist(board, word):
    ROWS = len(board)
    COLUMNS = len(board[0])
    visited = set()

    def dfs(row, column, index):
        if index == len(word):
            return True

        if  row < 0 or \
            row >= ROWS or \
            column < 0 or \
            column >= COLUMNS or \
            board[row][column] != word[index] or \
            (row, column) in visited:
            return False

        return (
            dfs(row + 1, column, index + 1) or \
            dfs(row - 1, column, index + 1) or \
            dfs(row, column + 1, index + 1) or \
            dfs(row, column - 1, index + 1)
        )

    for i in range(ROWS):
        for j in range(COLUMNS):
            if dfs(i,j):
                return True

    return False