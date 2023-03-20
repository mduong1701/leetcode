class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        result = ""

        for row in range(numRows):
            increment = numRows * 2 - 2
            