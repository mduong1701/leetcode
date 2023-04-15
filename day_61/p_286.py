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

        while queue:
            queueLength = len(queue)
            for _ in range(queueLength):
                