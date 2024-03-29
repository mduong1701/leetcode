class Solution:
    def numSquares(self, n):
        dp = [n for _ in range(n + 1)]
        dp[0] = 0

        for target in range(1, n + 1):
            for num in range(1, target + 1):
                square = num ** 2
                if square > target:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])
        
        return dp[n]