class Solution:
    def minFlips(self, s):
        # Initialize the final result to be the length of the string
        result = len(s)
        # Double the string
        s = s + s
        # Make 2 desired outcome strings 010101... 101010...
        desiredS1 = ""
        desiredS2 = ""
        for i in range(len(s)):
            
