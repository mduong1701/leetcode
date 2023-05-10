class Solution:
    def leastBricks(self, wall):

        countGap = {0: 0}

        for row in wall:

            width = 0
            for brick in row[:-1]:
                width += brick
                countGap[width] = 1 + countGap.get(width, 0)