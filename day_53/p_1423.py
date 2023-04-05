class Solution:
    def maxScore(self, cardPoints, k):
        # cardPoints = [ 1 , 2 , 3 , 4 , 5 , 6 , 1 ], k = 3
        # index          0   1   2   3   4   5   6
        #                l               r
        l = 0
        r = len(cardPoints) - k
        total = sum(cardPoints[r : ])
        result = total
        