import unittest
from subTree_of_another_tree import TreeNode, Solution

class TestSubTreeOfAnotherTree(unittest.TestCase):
    def test_subTreeofAnotherTree(self):
        # Test case 1: Both trees are empty
        s1 = None
        t1 = None
        self.assertTrue(Solution().subTreeofAnotherTree(s1, t1))

        # Test case 2: One tree is empty, the other is not
        s2 = None
        t2 = TreeNode(1)
        self.assertFalse(Solution().subTreeofAnotherTree(s2, t2))

        # Test case 3: t is a subtree of s
        s3 = TreeNode(3)
        s3.left = TreeNode(4)
        s3.right = TreeNode(5)
        s3.left.left = TreeNode(1)
        s3.left.right = TreeNode(2)

        t3 = TreeNode(4)
        t3.left = TreeNode(1)
        t3.right = TreeNode(2)

        self.assertTrue(Solution().subTreeofAnotherTree(s3, t3))

        # Test case 4: t is not a subtree of s
        s4 = TreeNode(3)
        s4.left = TreeNode(4)
        s4.right = TreeNode(5)
        s4.left.left = TreeNode(1)
        s4.left.right = TreeNode(2)

        t4 = TreeNode(4)
        t4.left = TreeNode(1)
        t4.right = TreeNode(3)

        self.assertFalse(Solution().subTreeofAnotherTree(s4, t4))

        # Test case 5: t is a subtree of s, but with different values
        s5 = TreeNode(3)
        s5.left = TreeNode(4)
        s5.right = TreeNode(5)
        s5.left.left = TreeNode(1)
        s5.left.right = TreeNode(2)

        t5 = TreeNode(4)
        t5.left = TreeNode(1)
        t5.right = TreeNode(2)
        t5.left.left = TreeNode(5)

        self.assertFalse(Solution().subTreeofAnotherTree(s5, t5))

if __name__ == '__main__':
    unittest.main(verbosity=2)