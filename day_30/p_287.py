def findDuplicate(nums):
    slow = 0
    fast = 0

    while True:
        slow = nums[slow]
        fast = nums[fast]
        fast = nums[fast]

        if slow == fast:
            break

    slow = 0

    while True:
        slow = nums[slow]
        fast = nums[fast]
        if slow == fast:
            return slow

print(findDuplicate([1,3,4,2,2]))
print(findDuplicate([3,1,3,4,2]))