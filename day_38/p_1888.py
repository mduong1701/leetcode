class Solution:
    def minFlips(self, s):
        # Initialize the final result to be the length of the string
        result = len(s)
        # length of original string
        lengthS = len(s)
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
        # Differences between s and desiredS1 and desired2
        diff1 = 0
        diff2 = 0
        # Sliding window
        for r in range(len(s)):
            if s[r] != desiredS1[r]:
                diff1 += 1
            if s[r] != desiredS2[r]:
                diff2 += 1
            if r - l + 1 > lengthS:
                if s[l] != desiredS1[l]:
                    diff1 -= 1
                if s[l] != desiredS2[l]:
                    diff2 -= 1
                l += 1
            