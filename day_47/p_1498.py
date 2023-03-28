class Solution:
    def numSubseq(self, nums, target):
        result = 0
        nums.sort()

        right = len(nums) - 1
        mod = 10**9 + 7

        for left in range(len(nums)):
            while (nums[left] + nums[right]) > target and left <= right:
                right -= 1
                