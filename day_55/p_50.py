class Solution:
    def myPow(self, x, n):
        def helper(base, power):
            if base == 0:
                return 0
            if power == 0:
                return 1
            
            result = helper(base, power // 2)
            result = result * result
            return base * result if power % 2 else result

        