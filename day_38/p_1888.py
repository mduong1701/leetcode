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
            desiredS1 += "1" if i % 2 == 0 else "0"
            desiredS2 += "0" if i % 2 == 0 else "1"
        # Left pointer
        l = 0
        # Sliding window
        for r in range(len(s)):
            
