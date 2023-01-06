def canPartition(nums):
    total = sum(nums)

    if total % 2 != 0:
        return False
    
    target = total / 2
    possibleSums = set()

    possibleSums.add(0)

    for i in range(len(nums) - 1, -1, -1):
        for oneSum in possibleSums:
            


