class Solution:
    def mincostTickets(self, days, costs):
        # days = [1, 4, 6, 7, 8, 20], costs = [2, 7, 15], [1, 7, 30]
        #         0  1  2  3  4  5                
        dp = {}
        # 5     2
        # 4     2 + 2 = 4
        # 3     INF
        for i in range(len(days) - 1, -1, -1):
            dp[i] = float('inf')
            for day, cost in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + day:
                    j += 1
                dp[i] = min(dp[i], cost + dp.get(j, 0))
        return dp[0]


