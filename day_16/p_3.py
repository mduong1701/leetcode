def longest(s):
    result = 0
    left = 0
    uniqueCharacters = set()

    for right in range(len(s)):
        while s[right] in uniqueCharacters:
            uniqueCharacters.remove(s[left])
            left += 1
        uniqueCharacters.add(s[right])
        result=max(result, len(s[left:right+1]))

    return result

print(longest("abcabcbb"))
print(longest("bbbbb"))
print(longest("pwwwkew"))