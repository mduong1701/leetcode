from locale import currency


class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtracking(curArr, start, sumLeft):
            if sumLeft == 0:
                result.append(curArr.copy())
            if sumLeft <= 0:
                return

            previous = -1
            for i in range(start, len(candidates)):
                if candidates[i] == previous:
                    continue

                curArr.append(candidates[i])
                backtracking(curArr, i + 1, target - candidates[i])
                curArr.pop()

                previous = candidates[i]

            