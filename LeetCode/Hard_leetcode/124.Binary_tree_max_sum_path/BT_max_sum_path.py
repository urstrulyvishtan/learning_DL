class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxSumPath(self, root):
        self.max_sum = float('-inf')
        self.maxSumPathHelper(root)
        return self.max_sum
    
    def maxSumPathHelper(self, root):
        if not root:
            return 0
        left = max(0, self.maxSumPathHelper(root.left))
        right = max(0, self.maxSumPathHelper(root.right))
        self.max_sum = max(self.max_sum, left + right + root.val)
        return max(left, right) + root.val
    