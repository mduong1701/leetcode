def longest(s):
    # b a b a d

    result = ""
    
    for i in range(len(s)):

        left = i
        right = i

        while left >= 0 and right < len(s) and s[left] == s[right]:
            if len(result) < right - left + 1:
                result = s[left : right + 1]
            left -= 1
            right += 1

        left = i
        right = i + 1

        while left >= 0 and right < len(s) and s[left] == s[right]:
            if len(result) < right - left + 1:
                result = s[left : right + 1]
            left -= 1
            right += 1
    
    return result

print(longest("babad"))
print(longest("cbbd"))

