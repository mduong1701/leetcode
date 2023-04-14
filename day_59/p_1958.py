class Solution:
    def checkMove(self, board, rMove, cMove, color):
        ROWS = len(board)
        COLS = len(board[0])

        DIRECTIONS = [[ 1, 0],[ -1, 0],[ 0, 1],[ 0, -1],[ 1, 1],[ -1, -1],[ 1, -1],[ -1, 1]]

        def move(x, y, color, direction):
            dx, dy = direction
            newX, newY = x + dx, y + dy

            while (0 <= newX < ROWS) and (0 <= newY < COLS):
                
