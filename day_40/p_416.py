def canPartition(nums):
    numSum = sum(nums)

    if numSum % 2 == 1:
        return False

    target = numSum // 2
    dp = set()
    dp.add(0)

    for i in range(len(nums)):
        tempDP = set()
        for num in dp:
            tempSum = num + nums[i]
            if tempSum == target:
                return True

            tempDP.add(num)

            if tempSum < target:
                tempDP.add(tempSum)

        dp = tempDP

    return True if target in dp else False

test = [14,9,8,4,3,2]
# test = [1,5,11,5]
print(canPartition(test))