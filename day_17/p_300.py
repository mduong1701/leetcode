def longestSub(nums):
    result = 1

    for i, num in enumerate(nums):
        if i > 0 and nums[i - 1] >= nums[i]:
            continue

        result += 1
