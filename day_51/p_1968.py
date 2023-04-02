class Solution:
    def rearrangeArray(self, nums):
        # [ 1 2 3 4 5]
        nums.sort()
        result = []
        left = 0
        right = len(nums) - 1

        while len(result) != len(nums):
            
