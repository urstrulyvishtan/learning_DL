import unittest
from binary_tree_order_traversal import TreeNode, Solution

class TestBinaryTreeOrderTraversal(unittest.TestCase):
    def test_levelOrder(self):
        # Test case 1: Empty tree
        root1 = None
        self.assertEqual(Solution().levelOrder(root1), [])

        # Test case 2: Tree with a single node
        root2 = TreeNode(1)
        self.assertEqual(Solution().levelOrder(root2), [[1]])

        # Test case 3: Tree with multiple levels
        root3 = TreeNode(3)
        root3.left = TreeNode(9)
        root3.right = TreeNode(20)
        root3.right.left = TreeNode(15)
        root3.right.right = TreeNode(7)
        self.assertEqual(Solution().levelOrder(root3), [[3], [9, 20], [15, 7]])

        # Test case 4: Tree with uneven levels
        root4 = TreeNode(1)
        root4.left = TreeNode(2)
        root4.left.left = TreeNode(4)
        root4.right = TreeNode(3)
        root4.right.right = TreeNode(5)
        self.assertEqual(Solution().levelOrder(root4), [[1], [2, 3], [4, 5]])

if __name__ == '__main__':
    unittest.main(verbosity=2)