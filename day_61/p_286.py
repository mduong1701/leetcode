from collections import deque

class Solution:
    def wallsAndGates(self, rooms):
        ROWS = len(rooms)
        COLUMNS = len(rooms[0])
        DIRECTIONS = [[1,0],[-1,0],[0,1],[0,-1]]

        visited = set()
        queue = deque()

        