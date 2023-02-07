def canJump(nums):
    length = len(nums)

    if length == 1 and nums[0] == 0:
        return True

    i = 0

    while i <= length:
        i += nums[i]
        if i == length:
            return True

    return False
