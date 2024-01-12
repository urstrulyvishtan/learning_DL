import unittest
from max_depth_binary_tree import TreeNode, Solution

class TestMaxDepthBinaryTree(unittest.TestCase):
    def test_maxDepth(self):
        # Test case 1: Empty tree
        root = None
        expected = 0
        solution = Solution()
        result = solution.maxDepth(root)
        self.assertEqual(result, expected)

        # Test case 2: Single node tree
        root = TreeNode(1)
        expected = 1
        solution = Solution()
        result = solution.maxDepth(root)
        self.assertEqual(result, expected)

        # Test case 3: Tree with multiple nodes
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        expected = 3
        solution = Solution()
        result = solution.maxDepth(root)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()