class Solution:
    def countBits(self, n):
        dp = [ 0 for _ in range(n + 1)]
        level = 1

        for i in range(1, n + 1):
            if 