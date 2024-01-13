class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class solution:
    def KthSmallest(self, root, k):
        if not root:
            return None
        stack = []
        while root:
            stack.append(root)
            root = root.left
        while k:
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        return None