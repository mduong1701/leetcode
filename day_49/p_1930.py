class Solution:
    def countPalindromicSubsequence(self, s):
        result = set()
        left = set()
        right = {}

        for character in s:
            right[character] = right.get(character, 0) + 1
        
        for i in range(len(s)):
            right[s[i]] -= 1

            if right[s[i]] == 0:
                del right[s[i]]

            for j in range(26):
                c = chr(ord(s[i]) + j)
                if c in left and c in right:
                    result.add((s[i], c))

            left.add(s[i])