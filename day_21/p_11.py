def maxArea(height):
    
    left = 0
    right = len(height) - 1
    area = 0

    while left < right:
        
