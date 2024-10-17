# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: # 1, 4, 5 , 1, 3, 4 , 2, 6 
        heap = []
        for i in range(len(lists)):
            if list[i]:
                heapq.heappush(heap, (lists[i].val, i, list[i])) # 1, 0, node(1), 1, 1, node(1), 2, 2, node(2)
        dummy = ListNode(0)
        current = dummy

        while heap:
            val, i, node = heapq.heappop(heap) # 1, 0, node(1)
            current.next = ListNode(val) # 1
            currernt = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
        
# init min-heap and push the first node of LL into the heap
# extract the smallest node from the heap and append it to the result
# push the next node from the same list into the heap
# continue this until the heap is empty
# return the merged list

# time complexity O(N log K)
# space complexity O(K)

# merge the LL in pair
# continue merging until only one list remains
# recursively merge two list at a time 
# after one round of merging halve the number of lists by merging two at a time
# continue until there's only one list remaining
# time complexity O(N log K)
# space complexity O(log K)