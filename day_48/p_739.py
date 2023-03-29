class Solution:
    def dailyTemperatures(self, temperatures):
        result = [0 for _ in range(len(temperatures))]
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                temperature, index = stack.pop()
                result[index] = t - temperature
            stack.append((t, i))

        return result