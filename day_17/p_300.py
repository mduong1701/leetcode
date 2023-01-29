def longestSub(nums):
    result = [ 1 for _ in range(len(nums))]

    for i in range(len(result)):
        for j in range(i):
            if nums[j] < nums[i]:
                result[i] = max(1, 1 + result[j])

    return max(result)



