class Solution:
    def searchRange(self, nums, target):
        pass

    def binarySearch(self, nums, target, leftBias):
        left = 0
        right = len(nums) - 1
        i = -1

        while left <= right:
            