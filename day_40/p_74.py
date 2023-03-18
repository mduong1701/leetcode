class Solution:
    def searchMatrix(self, matrix, target):
        top = 0
        bottom = len(matrix)
        middle = -1
        while top < bottom:
            middle = (top + bottom) // 2

            