from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: # 32ms, 14.5MB
    def levelOrder(self, root: TreeNode):
        res = []

        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range (qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res