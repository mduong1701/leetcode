class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        
        for i in range(len(s)):
            