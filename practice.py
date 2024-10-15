# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = [] # 7, 3
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop() 
        result = node.val

        if node.right:
            self._push_left(node.right)
        return result 

    def hasNext(self) -> bool:
        return len(self.stack)>0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# hasNext() check if there are more elements in the list
# next() return the next element from the list
# time complexity O(n)
# space complexity O(n)

# init the stack by pushing all from root to leftmost elements
# for each call to next() pop top node
# if pop has right child push all the leftmost node of right subtree into the stack

# time complexity O(1)
# space complexity O(h)