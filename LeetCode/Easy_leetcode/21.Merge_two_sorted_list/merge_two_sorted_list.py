class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        elif l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2