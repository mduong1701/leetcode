def wordBreak(s, wordDict):
    dp = [False for _ in range(len(s) + 1)]
    dp[-1] = True

    for i in range(len(s) - 1, -1, -1):
        for word in wordDict:
            if i + len(word) <= len(s) and s[i : i + len(word)] == word:
                dp[i] = dp[i + len(word)]
            if dp[i]:
                break
    
    return dp[0]

print(wordBreak("leetcode", ["leet","code"]))
print(wordBreak("applepenapple", ["apple","pen"]))
print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))