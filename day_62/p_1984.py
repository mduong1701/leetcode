class Solution:
    def minimumDifference(self, nums, k):
        nums.sort()
        # 1   4   7   9
        # l   r

        result = float('inf')

        l = 0
        r = k - 1

        while r < len(nums):
            result = min(result, nums[r] - nums[l])
            l += 1
            r += 1

        return result
