class Solution:
    def canPartition(self, nums):
        numSum = sum(nums)

        if numSum % 2 == 1:
            return False

        