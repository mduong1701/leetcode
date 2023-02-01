def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2
        
        if nums[middle] == target:
            return middle

        if nums[middle] >= nums[left]:
            if target > nums[middle] or target < nums[left]:
                left = middle + 1
            else:
                right = left - 1
        
        else:
            if target < nums[middle] or target > nums[right]:
                right = middle - 1