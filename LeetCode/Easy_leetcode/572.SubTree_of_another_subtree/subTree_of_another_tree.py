class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subTreeofAnotherTree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t: return True
        if not s or not t: return False
        return self.sameTree(s, t) or self.subTreeofAnotherTree(s.left, t) or self.subTreeofAnotherTree(s.right, t)
    def sameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
    
    