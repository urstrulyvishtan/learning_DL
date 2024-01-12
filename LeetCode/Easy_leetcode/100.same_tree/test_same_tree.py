import unittest
from same_tree import TreeNode, Solution

class TestSameTree(unittest.TestCase):
    def test_sameTree(self):
        # Test case 1: Both trees are empty
        p1 = None
        q1 = None
        self.assertTrue(Solution().sameTree(p1, q1))

        # Test case 2: One tree is empty, the other is not
        p2 = None
        q2 = TreeNode(1)
        self.assertFalse(Solution().sameTree(p2, q2))

        # Test case 3: Both trees have the same structure and values
        p3 = TreeNode(1)
        p3.left = TreeNode(2)
        p3.right = TreeNode(3)

        q3 = TreeNode(1)
        q3.left = TreeNode(2)
        q3.right = TreeNode(3)

        self.assertTrue(Solution().sameTree(p3, q3))

        # Test case 4: Both trees have different values
        p4 = TreeNode(1)
        p4.left = TreeNode(2)
        p4.right = TreeNode(3)

        q4 = TreeNode(1)
        q4.left = TreeNode(4)
        q4.right = TreeNode(3)

        self.assertFalse(Solution().sameTree(p4, q4))

        # Test case 5: Both trees have different structures
        p5 = TreeNode(1)
        p5.left = TreeNode(2)

        q5 = TreeNode(1)
        q5.right = TreeNode(2)

        self.assertFalse(Solution().sameTree(p5, q5))

if __name__ == '__main__':
    unittest.main(verbosity=2)