class Solution:
    def maxAlternatingSum(self, nums):
        sumEven = 0
        sumOdd = 0

        for i in range(len(nums) - 1, -1, -1):
            
