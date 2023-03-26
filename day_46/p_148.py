# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        left = head
        right = self.getMid(head)

        tmp = right.next
        right.next = None
        right = tmp

        leftPart = self.sortList(left)
        rightPart = self.sortList(right)

        return self.merge(leftPart, rightPart)

    def getMid(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, list1, list2):
        dummy = tail = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        