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
                    x += dx
                    y += dy

                    if x < 0 or x == ROWS or y < 0 or y == COLUMNS or (x, y) in visited or rooms[x][y] == -1:
                        continue

                    queue.append([x, y])
                    visited.add((x, y))
            
            distance += 1
