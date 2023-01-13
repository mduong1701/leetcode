# def permute(nums):
#     result = []
#     n = len(nums)

#     def dfs(first):
#         if first == n:
#             result.append(nums[:])
        
#         for i in range(first, n):
#             nums[first], nums[i] = nums[i], nums[first]
#             dfs(first + 1)
#             nums[first], nums[i] = nums[i], nums[first]


#     dfs(0)
#     return result

def permute(nums):
    result = []

    def dfs(array, permutation):
        if not array and permutation:
            result.append(permutation)
        else:
            for i in range(len(array)):
                newArray = array[:i] + array[i + 1:]
                newPermutation = permutation + [array[i]]
                dfs(newArray, newPermutation)
    
    dfs(nums, [])

    return result

print(permute([1,2,3]))