def wordBreak(s, wordDict):
    dp = [False for _ in range(len(s) + 1)]
    dp[-1] = True

    