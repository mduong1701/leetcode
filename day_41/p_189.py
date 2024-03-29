class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)

        def reverseArray(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverseArray(nums, 0, len(nums) - 1)
        reverseArray(nums, 0, k - 1)
        reverseArray(nums, k, len(nums) - 1)