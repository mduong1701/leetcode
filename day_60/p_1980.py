class Solution:
    def findDifferentBinaryString(self, nums):
        # nums = ["111","011","001"]
        numSet = {num for num in nums}

        def backtracking(index, current):
            if len(current) == index:
                result = "".join(current)
                return result if result not in numSet else None

            


        return backtracking(0, ["0" for _ in range(len(nums))])