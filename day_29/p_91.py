def numDecodings(s):
    dp = [0 for _ in range(len(s) + 1)]
    dp[-1] = 1

    