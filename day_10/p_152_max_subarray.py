def maxProduct(nums):

    result = max(nums) # 1 -9 2 [8] 0 -3 7 4 -6 5

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
