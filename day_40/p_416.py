class Solution:
    def canPartition(self, nums):
        numSum = sum(nums)

        if numSum % 2 == 1:
            return False

        target = numSum / 2
        dp = set()
        dp.add(0)

        

