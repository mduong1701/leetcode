def longestPalindrome(s):
    characterDict = {}
    result = 0
    for character in s:
        if character not in characterDict:
            characterDict[character] = 1
        else:
            characterDict[character] += 1
    
    for frequency in characterDict.values():
        result += ((frequency // 2) * 2)
        if result % 2 == 0 and frequency == 1:
            result += 1
    return result

print(longestPalindrome("abccccdd"))
print(longestPalindrome("a"))
print(longestPalindrome("Aa"))
print(longestPalindrome("bb"))
print(longestPalindrome("bba"))