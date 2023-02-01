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
            else:
                left = middle + 1
    
    return -1

print(search([4,5,6,7,0,1,2], 0))
print(search([4,5,6,7,0,1,2], 3))
print(search([], 0))