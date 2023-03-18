class Solution:
    def canPartition(self, nums):
        numSum = sum(nums)

        if numSum % 2 == 1:
            return False

        target = numSum / 2
        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            tempDP = set()
            for num in dp:
                if num + nums[i] == target:
                    return True

                if num + nums[i] < target:
                    tempDP.add(num + nums[i])
                    tempDP.add(num)

            dp = tempDP

        return False

