def longest(text1, text2):
    len1 = len(text1)
    len2 = len(text2)
    dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    

