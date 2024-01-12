import unittest
from merge_two_sorted_list import ListNode, Solution

class TestMergeTwoSortedLists(unittest.TestCase):
    def test_mergeTwoLists(self):
        # Test case 1: Both lists are empty
        l1 = None
        l2 = None
        expected = None
        solution = Solution()
        self.assertEqual(solution.mergeTwoLists(l1, l2), expected)

        # Test case 2: One list is empty
        l1 = None
        l2 = ListNode(1)
        expected = ListNode(1)
        solution = Solution()
        self.assertEqual(solution.mergeTwoLists(l1, l2).val, expected.val)
        self.assertIsNone(solution.mergeTwoLists(l1, l2).next)

        # Test case 3: Both lists have single node
        l1 = ListNode(1)
        l2 = ListNode(2)
        expected = ListNode(1)
        expected.next = ListNode(2)
        solution = Solution()
        self.assertEqual(solution.mergeTwoLists(l1, l2).val, expected.val)
        self.assertEqual(solution.mergeTwoLists(l1, l2).next.val, expected.next.val)
        self.assertIsNone(solution.mergeTwoLists(l1, l2).next.next)

        # Test case 4: Both lists have multiple nodes
        l1 = ListNode(1)
        l1.next = ListNode(3)
        l1.next.next = ListNode(5)
        l2 = ListNode(2)
        l2.next = ListNode(4)
        l2.next.next = ListNode(6)
        expected = ListNode(1)
        expected.next = ListNode(2)
        expected.next.next = ListNode(3)
        expected.next.next.next = ListNode(4)
        expected.next.next.next.next = ListNode(5)
        expected.next.next.next.next.next = ListNode(6)
        solution = Solution()
        self.assertEqual(solution.mergeTwoLists(l1, l2).val, expected.val)
        self.assertEqual(solution.mergeTwoLists(l1, l2).next.val, expected.next.val)
        self.assertEqual(solution.mergeTwoLists(l1, l2).next.next.val, expected.next.next.val)
        self.assertEqual(solution.mergeTwoLists(l1, l2).next.next.next.val, expected.next.next.next.val)
        self.assertEqual(solution.mergeTwoLists(l1, l2).next.next.next.next.val, expected.next.next.next.next.val)
        self.assertEqual(solution.mergeTwoLists(l1, l2).next.next.next.next.next.val, expected.next.next.next.next.next.val)
        self.assertIsNone(solution.mergeTwoLists(l1, l2).next.next.next.next.next.next)

if __name__ == '__main__':
    unittest.main()