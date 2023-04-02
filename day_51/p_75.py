class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums)
        i = 0

        def swap(a, b):
            nums[a], nums[b] = nums[b], nums[a]

        while i <= right:
            if nums[i] == 0:
                swap(left, i)
                left += 1
            elif nums[i] == 2:
                swap(right, i)
                right -= 1
                i -= 1
            i += 1
