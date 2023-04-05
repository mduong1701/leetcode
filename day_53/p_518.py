class Solution:
    def change(self, amount, coins):
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1

        for coinIndex in range(len(coins) - 1, -1, -1):
            nextDP = [0 for _ in range(amount + 1)]
            nextDP[0] = 1

            for i in range(1, amount + 1):
                nextDP[i] = dp[i]
                if i >= coins[coinIndex]:
                    nextDP[i] += nextDP[i - coins[coinIndex]]
