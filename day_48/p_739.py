class Solution:
    def dailyTemperatures(self, temperatures):
        result = [0 for _ in range(len(temperatures))]
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _, index = stack.pop()
                result[index] = i - index
            stack.append((t, i))

        return result