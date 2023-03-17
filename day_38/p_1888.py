class Solution:
    def minFlips(self, s):
        # Initialize the final result to be the length of the string
        result = len(s)
        # Double the string
        s = s + s
