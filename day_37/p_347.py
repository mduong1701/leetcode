class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        frequency = [ [] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        
