# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: # 1, 4, 5 , 1, 3, 4 , 2, 6 
        # Min-heap to store (node_value, list_index, node) for each linked list
        heap = []
        
        # Step 1: Push the head node of each linked list into the heap
        for i in range(len(lists)):
            if lists[i]:  # Check if the list is not None
                heappush(heap, (lists[i].val, i, lists[i]))  # Push only non-None nodes
        
        # Dummy node to start building the merged list
        dummy = ListNode(0)
        current = dummy
        
        # Step 2: While the heap is not empty, process the smallest element
        while heap:
            val, i, node = heappop(heap)  # Get the smallest node
            
            # Append it to the result list
            current.next = ListNode(val)
            current = current.next
            
            # Move to the next node in the same list and push it into the heap if it's not None
            if node.next:
                heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next  # Return the merged linked list

# init an empty list
# loop through each LL and extract all the values, append
# sort
# construct new LL from the sorted

# time complexity : O(N Log N)
# space complexity : O(N)

# init pq
# push the head of each LL to the heap
# heap is not empty then pop smallest and append to result. push the next node from same list into heap

# time complexity : O(N log K)
# space complexity : O(K)