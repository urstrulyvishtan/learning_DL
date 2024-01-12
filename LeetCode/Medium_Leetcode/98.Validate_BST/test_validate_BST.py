import unittest
from validate_BST import treeNode, solution

class TestValidateBST(unittest.TestCase):
    def test_valid_BST(self):
        # Create a valid binary search tree
        root = treeNode(2)
        root.left = treeNode(1)
        root.right = treeNode(3)
        sol = solution()
        self.assertTrue(sol.isValidBST(root))

    def test_invalid_BST(self):
        # Create an invalid binary search tree
        root = treeNode(5)
        root.left = treeNode(1)
        root.right = treeNode(4)
        root.right.left = treeNode(3)
        root.right.right = treeNode(6)
        sol = solution()
        self.assertFalse(sol.isValidBST(root))

    def test_empty_tree(self):
        # Test an empty tree
        root = None
        sol = solution()
        self.assertTrue(sol.isValidBST(root))

    def test_single_node(self):
        # Test a tree with a single node
        root = treeNode(1)
        sol = solution()
        self.assertTrue(sol.isValidBST(root))

if __name__ == '__main__':
    unittest.main()