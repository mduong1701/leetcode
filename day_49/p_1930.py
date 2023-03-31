class Solution:
    def countPalindromicSubsequence(self, s):
        result = set()
        left = set()
        right = {}

        