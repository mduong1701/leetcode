def combinationSum(candidates, target):
    result = []
    currentArray = []

    def dfs(i):
        if sum(currentArray) > target:
            return
        if sum(currentArray) == target:
            result.append(currentArray.copy())

        currentArray.append(candidates[i])
        dfs(i)
        currentArray.pop()
        dfs(i + 1)
