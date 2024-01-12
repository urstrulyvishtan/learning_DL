import unittest
from reverse_linked_list import ListNode, Solution

class TestReverseLinkedList(unittest.TestCase):
    def test_reverseList(self):
        # Test case 1: Empty list
        head = None
        expected = None
        solution = Solution()
        self.assertEqual(solution.reverseList(head), expected)

        # Test case 2: Single node
        head = ListNode(1)
        expected = ListNode(1)
        solution = Solution()
        self.assertEqual(solution.reverseList(head).val, expected.val)
        self.assertIsNone(solution.reverseList(head).next)

        # Test case 3: Multiple nodes
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        expected = ListNode(5)
        expected.next = ListNode(4)
        expected.next.next = ListNode(3)
        expected.next.next.next = ListNode(2)
        expected.next.next.next.next = ListNode(1)
        solution = Solution()
        self.assertEqual(solution.reverseList(head).val, expected.val)
        self.assertEqual(solution.reverseList(head).next.val, expected.next.val)
        self.assertEqual(solution.reverseList(head).next.next.val, expected.next.next.val)
        self.assertEqual(solution.reverseList(head).next.next.next.val, expected.next.next.next.val)
        self.assertEqual(solution.reverseList(head).next.next.next.next.val, expected.next.next.next.next.val)
        self.assertIsNone(solution.reverseList(head).next.next.next.next.next)

if __name__ == '__main__':
    unittest.main()