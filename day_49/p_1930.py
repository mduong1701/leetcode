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

            



            left.add(s[i])