class Solution:
    def findDifferentBinaryString(self, nums):
        # nums = ["111","011","001"]
        numSet = {num for num in nums}

        def backtracking(index, current):
            if len(current) == index:
                result = "".join(current)
                return result if result not in numSet else None

            temp = backtracking(index + 1, current)
            if temp:
                return temp

            current[index] = "1"

            temp = backtracking(index + 1, current)
            if temp:
                return temp

        return backtracking(0, ["0" for _ in range(len(nums))])