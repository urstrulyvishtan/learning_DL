class treeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class solution:
    def isValidBST(self, root):
        return self.helper(root, float('-inf'), float('inf'))
    
    def helper(self, root, min, max):
        if not root:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.helper(root.left, min, root.val) and self.helper(root.right, root.val, max)