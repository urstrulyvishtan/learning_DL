import unittest
from BT_max_sum_path import Solution, TreeNode

class TestSolution(unittest.TestCase):
    def test_maxSumPath(self):
        solution = Solution()

        # Test case 1
        #       1
        #      / \
        #     2   3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(solution.maxSumPath(root), 6)

        # Test case 2
        #       -10
        #       /  \
        #      9    20
        #          /  \
        #         15   7
        root = TreeNode(-10)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(solution.maxSumPath(root), 42)

        # Test case 3
        #       1
        #      / \
        #     2   3
        #    / \
        #   4   5
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(solution.maxSumPath(root), 15)

if __name__ == '__main__':
    unittest.main()