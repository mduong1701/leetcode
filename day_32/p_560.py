class Solution:
    def subarraySum(self, nums, k):
        i = 1
        while i < len(nums):
            nums[i] += nums[i - 1]

        count = 0

        for i in range(len(nums)):
            