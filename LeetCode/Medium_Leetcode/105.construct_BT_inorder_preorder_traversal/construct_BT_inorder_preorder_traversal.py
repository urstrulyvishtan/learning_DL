class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if not inorder or not preorder:
            return None
        root = TreeNode(preorder[0])
        root_index = inorder.index(root.val)
        root.left = self.buildTree(preorder[1: root_index+1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])
        return root