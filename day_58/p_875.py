import math

class Solution:
    def minEatingSpeed(self, piles, h):
        # piles = [3,6,7,11], h = 8
        result = float("inf")
        left = 1
        right = max(piles)

        while left <= right:
            middle = (left + right) // 2
            time = 0

            for pile in piles:
                time += math.ceil(pile / middle)
            
            if time > h:
                left = middle + 1
                continue
            
            result = min(result, middle)
            right = middle - 1

        return result