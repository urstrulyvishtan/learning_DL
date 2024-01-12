import unittest
from invert_binary_tree import TreeNode, Solution

class TestInvertBinaryTree(unittest.TestCase):
    def test_invertTree(self):
        # Test case 1: Empty tree
        root = None
        expected = None
        solution = Solution()
        result = solution.invertTree(root)
        self.assertEqual(result, expected)

        # Test case 2: Single node tree
        root = TreeNode(1)
        expected = TreeNode(1)
        solution = Solution()
        result = solution.invertTree(root)
        self.assertEqual(result.val, expected.val)
        self.assertIsNone(result.left)
        self.assertIsNone(result.right)

        # Test case 3: Tree with multiple nodes
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)

        expected = TreeNode(4)
        expected.left = TreeNode(7)
        expected.right = TreeNode(2)
        expected.left.left = TreeNode(9)
        expected.left.right = TreeNode(6)
        expected.right.left = TreeNode(3)
        expected.right.right = TreeNode(1)

        solution = Solution()
        result = solution.invertTree(root)

        self.assertEqual(result.val, expected.val)
        self.assertEqual(result.left.val, expected.left.val)
        self.assertEqual(result.right.val, expected.right.val)
        self.assertEqual(result.left.left.val, expected.left.left.val)
        self.assertEqual(result.left.right.val, expected.left.right.val)
        self.assertEqual(result.right.left.val, expected.right.left.val)
        self.assertEqual(result.right.right.val, expected.right.right.val)

if __name__ == '__main__':
    unittest.main()