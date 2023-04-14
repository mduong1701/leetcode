class Solution:
    def findDifferentBinaryString(self, nums):
        # nums = ["111","011","001"]
        numSet = {num for num in nums}

        