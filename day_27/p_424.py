def character(s, k):
    result = 0
    count = {}
    maxF = 0
    left = 0

    for right in range(len(s)):
        count[s[right]] = 1 + count.get(s[right], 0)