def permute(nums):
    result = []

    def dfs(array, permutation):
        if not array and permutation:
            result.append(permutation)
        else:
            for i in range(len(array)):
                newPermutation = permutation + [array[i]]
                newArray = array[:i] + array[i+1:]
                dfs(newArray, newPermutation)

    dfs(nums, [])

    return result

print(permute([1,2,3]))