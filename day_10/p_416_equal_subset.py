def canPartition(nums):
    total = sum(nums)

    if total % 2 != 0:
        return False
    
    target = total / 2
    possibleSums = set()

    possibleSums.add(0)

    for i in range(len(nums) - 1, -1, -1):
        newDP = set()
        for oneSum in possibleSums:
            newDP.add(oneSum)
            newDP.add(oneSum + nums[i])
        possibleSums = newDP
        if target in possibleSums:
            return True
    
    return False

print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))



