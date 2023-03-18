class Solution:
    def searchMatrix(self, matrix, target):
        top = 0
        bottom = len(matrix)
        middle = -1
        while top <= bottom:
            middle = (top + bottom) // 2

            if target < matrix[middle][0]:
                bottom = middle - 1
            elif target > matrix[middle][-1]:
                top = middle + 1
            else:
                break

        l = 0
        r = len(matrix[0])

        while l <= r:
            m = (l + r) // 2

            