class Solution:
    def mincostTickets(self, days, costs):
        # days = [1, 4, 6, 7, 8, 20], costs = [2, 7, 15], [1, 7, 30]
        #         0  1  2  3  4  5                
        dp = {}
        #
        for i in range(len(days) - 1, -1, -1):
            dp[i] = float('inf')
            

