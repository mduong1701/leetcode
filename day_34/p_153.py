class Solution:
    def findMin(self, nums):
        result = nums[0]

        left = 0
        right = len(nums)

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break

            middle = (left + right) // 2
            result = min(result, nums[middle])

            if nums[left] >= nums[middle]:
                left = middle + 1
            else:
                right = middle - 1

        return result