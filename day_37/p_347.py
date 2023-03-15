class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        frequency = [ [] for _ in range(len(nums) + 1)]

        
