class Solution:
    def minimumTotal(self, triangle):
        dp = [0 for _ in range(len(triangle[-1]) + 1)]

        