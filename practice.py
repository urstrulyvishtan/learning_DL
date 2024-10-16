# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left if left else right

# if current node is none return none end of branch
# if current node matches p or q return that node potential LCA
# traverse left subtree
# traverse right subtree
# if both right and left subtrees return Non none value the current node is LCA(both p and q are in diffreent branches)
# if one of the subtree valid node and other returns none propagate valid node upwards

# time complexity O(n)
# space complexity O(h)

# 3, 5, 1, 6, 2, 0, 8, none, none, 7, 4 p = 5 q = 1

# root = 3, root = 5 = p returns root
# root = 1, return root
# LCA is 3

# traverse tree once and store the parent of each node in the dict
# starting from nodes p and q we'll trace thier paths to the root
# store the nodes encountered
# first common node in both the path is LCA

# dict{3: None, 5:3, 1:3, 6:5, 2:5, 0:1, 8:1, 7:2, 4:2}
# path p = 5 path = {5,3}
# path q = 1 move the parent q = 3
# q= 3 which is in the path LCA is 3

# time complexity and space complexity O(n)