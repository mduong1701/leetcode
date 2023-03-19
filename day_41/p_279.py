class Solution:
    def numSquares(self, n):
        dp = [n for _ in range(n + 1)]
        dp[0] = 0

        