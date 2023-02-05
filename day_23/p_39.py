def combinationSum(candidates, target):
    result = []
    currentArray = []

    def dfs(i):
        if i == len(candidates) or sum(currentArray) > target:
            return
        if sum(currentArray) == target:
            result.append(currentArray.copy())
            return

        currentArray.append(candidates[i])
        dfs(i)
        currentArray.pop()
        dfs(i + 1)

    dfs(0)

    return result
