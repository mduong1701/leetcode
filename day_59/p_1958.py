class Solution:
    def checkMove(self, board, rMove, cMove, color):
        ROWS = len(board)
        COLS = len(board[0])

        DIRECTIONS = [[ 1, 0],[ -1, 0],[ 0, 1],[ 0, -1],[ 1, 1],[ -1, -1],[ 1, -1],[ -1, 1]]

        def move(x, y, color, direction):
            dx, dy = direction
            newX, newY = x + dx, y + dy
            length = 1

            while (0 <= newX < ROWS) and (0 <= newY < COLS):
                length += 1
                if board[newX][newY] == '.':
                    return False
                if board[newX][newY] == color:
                    return length >= 3
                
                newX += dx
                newY += dy
            
            return False

        for direction in DIRECTIONS:
            if move(rMove, cMove, color, direction):
                return True

        return False
