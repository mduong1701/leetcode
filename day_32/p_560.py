class Solution:
    def subarraySum(self, nums, k):
        result = 0
        dic = { 0 : 1}
        preSum = 0

        for num in nums:
            preSum += num
            diff = preSum - k
            result += dic.get(diff, 0)
            dic[preSum] = 1 + dic.get(preSum, 0)

        return result