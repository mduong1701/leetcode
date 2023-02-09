def numTrees(n):

    dp = [1 for _ in range(n + 1)]

    for numNodes in range(2, n + 1):
        total = 0
        for root in range(1, numNodes + 1):
            left = root - 1
            right = numNodes - root
            total += dp[left] + dp[right]
        dp[numNodes] = total

    return dp[-1]

