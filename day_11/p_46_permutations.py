def permute(nums):
    result = []
    n = len(nums)

    def dfs(first):
        if first == n:
            result.append(nums[:])
        
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            dfs(first + 1)
            nums[first], nums[i] = nums[i], nums[first]


    dfs(0)
    return result

print(permute([1,2,3]))