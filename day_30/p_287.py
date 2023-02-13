def findDuplicate(self, nums):
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
        fast = nums[fast]
        if slow == fast:
            return slow

        