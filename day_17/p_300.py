def longestSub(nums):
    result = [ 1 for _ in range(len(nums))]

    for i in range(len(result)):
        for j in range(i):
            if nums[j] < nums[i]:
                result[i] = max(1, 1 + result[j])

    return max(result)

print(longestSub([10,9,2,5,3,7,101,18]))
print(longestSub([0,1,0,3,2,3]))
print(longestSub([7,7,7,7,7,7,7]))

