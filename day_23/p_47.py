def permute(nums):

    result = []
    currentA = []

    count = { n : 0 for n in nums}
    for num in nums:
        count[num] += 1

    def dfs():
        if len(currentA) == len(nums):
            result.append(currentA.copy())
            return

        for number in count:
            if count[number] > 0:
                currentA.append(number)
                count[number] -= 1

                dfs()

                currentA.pop()
                count[number] += 1

    dfs()

    return result