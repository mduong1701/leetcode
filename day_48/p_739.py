class Solution:
    def dailyTemperatures(self, temperatures):
        result = [0 for _ in range(len(temperatures))]
        stack = []

        for i, t in enumerate(temperatures):
            stack.append((t, i))

        return result