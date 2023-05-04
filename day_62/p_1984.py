class Solution:
    def minimumDifference(self, nums, k):
        nums.sort()
        # 1   4   7   9
        # l   r

        result = float('inf')

        l = 0
        r = k - 1

        
