import unittest
from remove_nth_node import ListNode, Solution

class TestRemoveNthNode(unittest.TestCase):
    def test_removeNthfromEnd(self):
        # Test case 1: Remove the only node in the list
        head = ListNode(1)
        n = 1
        expected = None
        solution = Solution()
        result = solution.removeNthfromEnd(head, n)
        self.assertEqual(result, expected)

        # Test case 2: Remove the last node in the list
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        n = 1
        expected = ListNode(1)
        expected.next = ListNode(2)
        solution = Solution()
        result = solution.removeNthfromEnd(head, n)
        self.assertEqual(result.val, expected.val)
        self.assertEqual(result.next.val, expected.next.val)
        self.assertIsNone(result.next.next)

        # Test case 3: Remove the first node in the list
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        n = 3
        expected = ListNode(2)
        expected.next = ListNode(3)
        solution = Solution()
        result = solution.removeNthfromEnd(head, n)
        self.assertEqual(result.val, expected.val)
        self.assertEqual(result.next.val, expected.next.val)
        self.assertIsNone(result.next.next)

        # Test case 4: Remove a node in the middle of the list
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        n = 2
        expected = ListNode(1)
        expected.next = ListNode(2)
        expected.next.next = ListNode(4)
        solution = Solution()
        result = solution.removeNthfromEnd(head, n)
        self.assertEqual(result.val, expected.val)
        self.assertEqual(result.next.val, expected.next.val)
        self.assertEqual(result.next.next.val, expected.next.next.val)
        self.assertIsNone(result.next.next.next)

if __name__ == '__main__':
    unittest.main()