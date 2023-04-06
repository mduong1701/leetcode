# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head

        length = 1
        tail = head

        while tail.next:
            length += 1
            tail = tail.next

        k = k % length
        
        cur = head
        for _ in range(length - k - 1):
            cur = cur.next

        
