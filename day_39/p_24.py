class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0, head)

        prev = dummy
        curr = head

        while curr and curr.next:
            second = curr.next
            nxtPair = curr.next.next

            