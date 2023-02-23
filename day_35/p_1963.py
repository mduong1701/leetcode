class Solution:
    def minSwaps(self, s):
        closeNum = 0
        closeMax = 0

        for character in s:
            if character == "]":
                closeNum += 1
            else:
                closeNum -= 1
            
            closeMax = max(closeMax, closeNum)

        return (closeMax + 1) // 2
