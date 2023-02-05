def permute(nums):

    result = []
    currentA = []

    count = { n : 0 for n in nums}
    for num in nums:
        count[num] += 1

    def dfs():
        if len(currentA) == len(nums):
            result.append(currentA)

        