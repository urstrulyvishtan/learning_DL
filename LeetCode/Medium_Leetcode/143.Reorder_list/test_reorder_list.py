import unittest
from reorder_list import ListNode, Solution

class TestReorderList(unittest.TestCase):
    def test_reorderList(self):
        # Test case 1: Empty list
        head = None
        expected = None
        solution = Solution()
        solution.reorderList(head)
        self.assertEqual(head, expected)

        # Test case 2: List with a single node
        head = ListNode(1)
        expected = ListNode(1)
        solution = Solution()
        solution.reorderList(head)
        self.assertEqual(head.val, expected.val)
        self.assertIsNone(head.next)

        # Test case 3: List with even number of nodes
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        expected = ListNode(1)
        expected.next = ListNode(4)
        expected.next.next = ListNode(2)
        expected.next.next.next = ListNode(3)
        solution = Solution()
        solution.reorderList(head)
        self.assertEqual(head.val, expected.val)
        self.assertEqual(head.next.val, expected.next.val)
        self.assertEqual(head.next.next.val, expected.next.next.val)
        self.assertEqual(head.next.next.next.val, expected.next.next.next.val)
        self.assertIsNone(head.next.next.next.next)

        # Test case 4: List with odd number of nodes
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        expected = ListNode(1)
        expected.next = ListNode(5)
        expected.next.next = ListNode(2)
        expected.next.next.next = ListNode(4)
        expected.next.next.next.next = ListNode(3)
        solution = Solution()
        solution.reorderList(head)
        self.assertEqual(head.val, expected.val)
        self.assertEqual(head.next.val, expected.next.val)
        self.assertEqual(head.next.next.val, expected.next.next.val)
        self.assertEqual(head.next.next.next.val, expected.next.next.next.val)
        self.assertEqual(head.next.next.next.next.val, expected.next.next.next.next.val)
        self.assertIsNone(head.next.next.next.next.next)

if __name__ == '__main__':
    unittest.main()