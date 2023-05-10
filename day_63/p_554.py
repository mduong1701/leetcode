class Solution:
    def leastBricks(self, wall):

        countGap = {0: 0}

        for row in wall:

            length = 0
            for brick in row:
                
