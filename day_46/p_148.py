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

        