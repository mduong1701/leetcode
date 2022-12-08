def pivotIndex(nums):
    leftSum, rightSum, sum = 0, 0, 0
    for i in range(len(nums)):
        sum += nums[i]
    for j in range(len(nums)):
        rightSum = sum - nums[j] - leftSum
        if leftSum == rightSum:
            return j
        leftSum += nums[j]
    return -1

print(pivotIndex([1,7,3,6,5,6]))
print(pivotIndex([1,2,3]))
print(pivotIndex([2,1,-1]))