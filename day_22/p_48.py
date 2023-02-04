def rotate(matrix):
    
    left = 0
    right = len(matrix) - 1
    top = 0
    bottom = len(matrix) - 1

    while left <= right:
        for i in range(left, right + 1):
            temp = matrix[top][i]
            matrix[top][i] = matrix[bottom][i]
            matrix[bottom][i] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top][right - i]
            matrix[top][right - i] = temp
