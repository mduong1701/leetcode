def rob(nums):
    return max(helper(nums[:-1]), helper(nums[1:]), nums[0])

def helper(nums):
    # 0      0     1     2     3      4
    #rob1  rob2   num
    #      rob1   rob2  num

    rob1 = 0
    rob2 = 0

    for num in nums:
        newRob = max(rob1 + num, rob2)
        rob1 = rob2
        rob2 = newRob

    return rob2
