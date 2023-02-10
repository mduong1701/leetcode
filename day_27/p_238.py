def product(nums):
    result = [1 for _ in range(len(nums))]

    prefix = 1
    for i in range(len(nums)):
        