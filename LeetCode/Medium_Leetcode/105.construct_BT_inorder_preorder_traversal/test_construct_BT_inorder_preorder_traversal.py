import unittest
from construct_BT_inorder_preorder_traversal import Solution, TreeNode
class TestSolution(unittest.TestCase):
    def test_buildTree(self):
        solution = Solution()

        # Test case 1
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        expected_output = TreeNode(3)
        expected_output.left = TreeNode(9)
        expected_output.right = TreeNode(20)
        expected_output.right.left = TreeNode(15)
        expected_output.right.right = TreeNode(7)
        self.assertEqual(solution.buildTree(preorder, inorder), expected_output)

        # Test case 2
        preorder = [1, 2, 3]
        inorder = [2, 1, 3]
        expected_output = TreeNode(1)
        expected_output.left = TreeNode(2)
        expected_output.right = TreeNode(3)
        self.assertEqual(solution.buildTree(preorder, inorder), expected_output)

        # Test case 3
        preorder = [1, 2, 3, 4, 5]
        inorder = [5, 4, 3, 2, 1]
        expected_output = TreeNode(1)
        expected_output.left = TreeNode(2)
        expected_output.left.left = TreeNode(3)
        expected_output.left.left.left = TreeNode(4)
        expected_output.left.left.left.left = TreeNode(5)
        self.assertEqual(solution.buildTree(preorder, inorder), expected_output)

if __name__ == '__main__':
    unittest.main()