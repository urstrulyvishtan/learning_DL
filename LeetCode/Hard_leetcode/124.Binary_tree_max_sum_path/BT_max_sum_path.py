class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxSumPath(self, root):
        res= [root.val]

        def maxSumPathHelper(root):
            if not root:
                return 0
            leftMax = max(0, maxSumPathHelper(root.left))
            rightMax = max(0, maxSumPathHelper(root.right))
            
            res[0] = max(res[0], root.val + leftMax+ rightMax)

            return root.val + max(leftMax, rightMax)
        
        maxSumPathHelper(root)
        return res[0]
    