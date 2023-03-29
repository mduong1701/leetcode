class Solution:
    def dailyTemperatures(self, temperatures):
        result = [0 for _ in range(len(temperatures))]
        stack = []

        