class Solution:
    def minimumTotal(self, triangle):
        dp = [0 for _ in range(len(triangle[-1]) + 1)]

        for i in range(len(triangle), 0, -1):
            temp = triangle[i - 1].copy()

            for j in range(len(temp)):
                temp[j] += min(dp[j], dp[j + 1])
            
            dp = temp

        return dp[0]

