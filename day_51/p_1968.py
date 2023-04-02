class Solution:
    def rearrangeArray(self, nums):
        # [ 1 2 3 4 5]
        nums.sort()
        result = []
        left = 0
        right = len(nums) - 1

        while len(result) != len(nums):
            result.append(nums[left])
            left += 1

            if left <= right:
                result.append(nums[right])
                right -= 1
        
        return result
