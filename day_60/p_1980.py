class Solution:
    def findDifferentBinaryString(self, nums):
        # nums = ["111","011","001"]
        numSet = {num for num in nums}

        def backtracking(index, current):
            pass

        return backtracking(0, ["0" for _ in range(len(nums))])