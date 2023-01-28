def maxProduct(nums):
    result = max(nums)
    curMax = 1
    curMin = 1

    for num in nums:
        if num == 0:
            curMax = 1
            curMin = 1
        else:
            temp = curMax
            curMax = max(curMax * num, curMin * num, num)
            curMin = min(temp * num, curMin * num, num)
            result = max(result, curMax)

    return result

print(maxProduct([2,3,-2,4]))