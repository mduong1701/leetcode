import heapq

class Solution:
    def swimInWater(self, grid):
        N = len(grid)
        visited = set()
        minHeap = [[grid[0][0], 0, 0]]
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        visited.add((0, 0))

        while minHeap:
            elevation, x, y = heapq.heappop(minHeap)

            for direction in directions:
                dX, dY = direction
                newX = x + dX
                newY = y + dY

                if newX < 0 or newX == N or newY < 0 or newY == N or (newX, newY) in visited:
                    continue

                visited.add((newX, newY))

                


