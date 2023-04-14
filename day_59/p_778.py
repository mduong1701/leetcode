class Solution:
    def swimInWater(self, grid):
        N = len(grid)
        visited = set()
        minHeap = [[grid[0][0], 0, 0]]

        

