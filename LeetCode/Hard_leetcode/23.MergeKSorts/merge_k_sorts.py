class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        if not lists or lists == 0: return None
        while(len(lists) > 1):
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                merged.append(self.mergeTwoLists(l1, l2))
            lists = merged

        return lists[0]
    
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        while(l1 and l2):
            if(l1.val < l2.val):
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        if(l1): current.next = l1
        if(l2): current.next = l2

        return dummy.next
