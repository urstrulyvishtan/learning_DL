class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution:
    def removeNthfromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = head
        while n > 0 and second:
            second = second.next
            n -= 1

        while second:
            first = first.next
            second = second.next

        first.next = first.next.next
        return dummy.next