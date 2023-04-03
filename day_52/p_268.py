class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        expectedSum = n * (n - 1) / 2
        realSum = sum(nums)
        return expectedSum - realSum