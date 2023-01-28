def threeSum(nums):
    nums.sort()

    visited = set()

    result = []

    for i in range(len(nums) - 2):
        if nums[i] in visited:
            continue

        visited.add(nums[i])

        numSet = set()
        for j in range(i + 1, len(nums)):
            dif = 0 - nums[i] - nums[j]
            if dif not in numSet:
                numSet.add(nums[j])
            else:
                result.append([nums[i], nums[j], dif])
    
    return result




print(threeSum([-1,0,1,2,-1,-4]))