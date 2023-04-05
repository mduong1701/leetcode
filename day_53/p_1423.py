class Solution:
    def maxScore(self, cardPoints, k):
        # cardPoints = [ 1 , 2 , 3 , 4 , 5 , 6 , 1 ], k = 3
        # index          0   1   2   3   4   5   6
        #                l               r
        l = 0
        r = len(cardPoints) - k
        total = sum(cardPoints[r : ])
        result = total

        while r < len(cardPoints):
            total += (cardPoints[l] - cardPoints[r])
            result = max(result, total)
            l += 1
            r += 1

        return result