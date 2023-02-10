def spiral(matrix):
    left = 0
    right = len(matrix[0]) - 1

    top = 0
    bottom = len(matrix) - 1

    result = []

    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if len(result) == (len(matrix) * len(matrix[0])):
            break

        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1
