class Solution:
    def searchRange(self, nums, target):
        leftIndex = self.binarySearch(nums, target, True)
        rightIndex = self.binarySearch(nums, target, False)

        return [leftIndex, rightIndex]

    def binarySearch(self, nums, target, leftBias):
        left = 0
        right = len(nums) - 1
        i = -1

        while left <= right:
            middle = (left + right) // 2
            if target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
            else:
                i = middle
                if leftBias:
                    right = middle - 1
                else:
                    left = middle + 1
        
        return i