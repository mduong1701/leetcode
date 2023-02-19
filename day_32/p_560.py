class Solution:
    def subarraySum(self, nums, k):
        i = 1
        while i < len(nums):
            nums[i] += nums[i - 1]

        count = 0
        visited = set()

        for i in range(len(nums)):
            if nums[i] == k or (k - nums[i] in visited):
                count += 1
            visited.add(nums[i])

        return count