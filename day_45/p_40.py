class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtracking(curArr, start, sumLeft):
            if sumLeft == 0:
                result.append(curArr.copy())
            if sumLeft <= 0:
                return

            
