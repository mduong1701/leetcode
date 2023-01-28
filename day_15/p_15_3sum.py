def threeSum(nums):
    nums.sort()

    visited = set()

    result = []

    for i in range(len(nums) - 2):
        if nums[i] in visited:
            continue

        visited.add(nums[i])

        left = i + 1
        right = len(nums) - 1

        dif = 0 - nums[i]
        while left < right:
            if dif > nums[left] + nums[right]:
                left += 1
            elif dif < nums[left] + nums[right]:
                right -= 1
            else:
                result.append([nums[i],nums[left],nums[right]])

    return result




print(threeSum([-1,0,1,2,-1,-4]))