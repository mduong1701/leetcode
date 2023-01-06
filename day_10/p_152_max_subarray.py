def maxProduct(nums):
    result = max(nums)
    curMin = 1
    curMax = 1

    for num in nums:
        tmp = curMin
        curMin = min(num, num * curMin, num * curMax)
        curMax = max(num, num * tmp, num * curMax)
        result = max(result, curMax)
        
    return result

print(maxProduct([2,3,-2,4]))
print(maxProduct([-2,0,-1]))
