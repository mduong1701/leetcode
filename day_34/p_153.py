class Solution:
    def findMin(self, nums):
        result = nums[0]

        left = 0
        right = len(nums)

        while left <= right:
            