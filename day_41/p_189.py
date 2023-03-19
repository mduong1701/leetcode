class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)

        def reverseArray(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

                