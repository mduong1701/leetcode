class Solution:
    def minEatingSpeed(self, piles, h):
        # piles = [3,6,7,11], h = 8
        result = float("inf")
        left = 0
        right = max(piles)

        
