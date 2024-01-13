from collections import deque
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        idx_map = {}
        for index in range(0, len(inorder)): idx_map[inorder[index]] = index
        preorder = deque(preorder)
        return self.helper(0, len(preorder) - 1, preorder, inorder, idx_map)

    def helper(self,left, right, preorder, inorder, idx_map):
        if left > right: return None
        root_val = preorder.popleft()
        root = TreeNode(root_val)
        #print(root_val, left,right,preorder,inorder)
        root.left = self.helper(left,idx_map[root_val]-1, preorder,inorder, idx_map)
        root.right = self.helper(idx_map[root_val]+1, right, preorder,inorder, idx_map)
        return root
    