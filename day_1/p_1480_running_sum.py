def runningSum(nums):
    result = [nums[0]] * len(nums)
    for i in range(1, len(nums)):
        result[i] = result[i - 1] + nums[i]
    return result

print(runningSum([1,2,3,4]))
print(runningSum([1,1,1,1,1]))
print(runningSum([3,1,2,10,1]))
print(runningSum([1]))