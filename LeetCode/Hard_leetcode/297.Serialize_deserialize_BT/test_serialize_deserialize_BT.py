import unittest
from serialize_deserialize_BT import TreeNode, Solution

class TestSolution(unittest.TestCase):
    def test_serialize_deserialize(self):
        # Test case 1: Tree with single node
        root = TreeNode(1)
        solution = Solution()
        serialized = solution.serialize(root)
        deserialized = solution.deserialize(serialized)
        self.assertEqual(root.val, deserialized.val)
        self.assertIsNone(deserialized.left)
        self.assertIsNone(deserialized.right)

        # Test case 2: Tree with multiple nodes
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        solution = Solution()
        serialized = solution.serialize(root)
        deserialized = solution.deserialize(serialized)
        self.assertEqual(root.val, deserialized.val)
        self.assertEqual(root.left.val, deserialized.left.val)
        self.assertEqual(root.right.val, deserialized.right.val)
        self.assertEqual(root.right.left.val, deserialized.right.left.val)
        self.assertEqual(root.right.right.val, deserialized.right.right.val)
        self.assertIsNone(deserialized.left.left)
        self.assertIsNone(deserialized.left.right)
        self.assertIsNone(deserialized.right.left.left)
        self.assertIsNone(deserialized.right.left.right)
        self.assertIsNone(deserialized.right.right.left)
        self.assertIsNone(deserialized.right.right.right)

if __name__ == '__main__':
    unittest.main()