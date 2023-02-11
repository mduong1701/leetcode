def numDecodings(s):
    dp = [0 for _ in range(len(s) + 1)]
    dp[-1] = 1

    for i in range(len(s) - 1, -1, -1):
        if s[i] != "0":
            dp[i] = dp[i + 1]
        if (i + 1 < len(s)) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
            dp[i] += dp[i+2]

    return dp[0]