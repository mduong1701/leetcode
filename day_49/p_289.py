class Solution:
    def gameOfLife(self, board):
        # Original      New         Value
        #    0           0            4
        #    0           1            5
        #    1           0            6
        #    1           1            7

        ROWS = len(board)
        COLS = len(board[0])

        def neighbors(row, column):
            result = 0
            for r in range(row - 1, row + 2):
                for c in range(column - 1, column + 2):
                    if (r == row and c == column) or r < 0 or c < 0 or r == ROWS or c == COLS:
                        continue
                    if board[r][c] in [1, 6, 7]:
                        result += 1
            return result

        for row in range(ROWS):
            for column in range(COLS):
                numNeighbors = neighbors(row, column)
                if numNeighbors == 3:
                    if board[row][column] == 0:
                        board[row][column] = 5
                    elif board[row][column] == 1:
                        board[row][column] = 7
                elif numNeighbors == 2:
                    if board[row][column] == 1:
                        board[row][column] = 7
                    elif board[row][column] == 0:
                        board[row][column] = 4
                else:
                    if board[row][column] == 0:
                        board[row][column] = 4
                    elif board[row][column] == 1:
                        board[row][column] = 6

        for row in range(ROWS):
            for column in range(COLS):
                if board[row][column] in [4,6]:
                    board[row][column] = 0
                else: 
                    board[row][column] = 1