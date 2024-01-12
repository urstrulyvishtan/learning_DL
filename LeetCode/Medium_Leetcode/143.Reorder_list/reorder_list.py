class ListNode:
    def __init__(self, val=0, next =None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head)-> None:
        if not head:
            return None
        # Find the middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Reverse the second half of the list
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        # Merge two lists
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        return head