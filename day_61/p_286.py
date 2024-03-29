from collections import deque

class Solution:
    def wallsAndGates(self, rooms):
        ROWS = len(rooms)
        COLUMNS = len(rooms[0])
        DIRECTIONS = [[1,0],[-1,0],[0,1],[0,-1]]

        visited = set()
        queue = deque()

        for row in range(ROWS):
            for column in range(COLUMNS):
                if rooms[row][column] == 0:
                    queue.append([row, column])
                    visited.add((row, column))

        distance = 0
        while queue:
            queueLength = len(queue)

            for _ in range(queueLength):
                x, y = queue.popleft()
                rooms[x][y] = distance
                for dx, dy in DIRECTIONS:
                    newX = x + dx
                    newY = y + dy

                    if newX < 0 or newX == ROWS or newY < 0 or newY == COLUMNS or (newX, newY) in visited or rooms[newX][newY] == -1:
                        continue

                    queue.append([newX, newY])
                    visited.add((newX, newY))
            
            distance += 1
