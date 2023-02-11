def uniquePaths(self, m, n):
    dp = [1 for _ in range(n)]

    for i in range(m - 1):
        temp = [1 for _ in range(n)]

        for j in range(n - 2, -1, -1):
            temp[j] = temp[j + 1] + dp[j]

        dp = temp

    return dp[0]