import unittest
from merge_k_sorts import ListNode, Solution

class TestMergeKSorts(unittest.TestCase):
    def test_mergeKLists(self):
        # Test case 1: Empty list
        lists = []
        expected = None
        solution = Solution()
        result = solution.mergeKLists(lists)
        self.assertEqual(result, expected)

        # Test case 2: Single list with one node
        lists = [ListNode(1)]
        expected = ListNode(1)
        solution = Solution()
        result = solution.mergeKLists(lists)
        self.assertEqual(result.val, expected.val)
        self.assertIsNone(result.next)

        # Test case 3: Single list with multiple nodes
        lists = [ListNode(1), ListNode(2), ListNode(3)]
        expected = ListNode(1)
        expected.next = ListNode(2)
        expected.next.next = ListNode(3)
        solution = Solution()
        result = solution.mergeKLists(lists)
        self.assertEqual(result.val, expected.val)
        self.assertEqual(result.next.val, expected.next.val)
        self.assertEqual(result.next.next.val, expected.next.next.val)
        self.assertIsNone(result.next.next.next)

        # Test case 4: Multiple lists with multiple nodes
        lists = [ListNode(1), ListNode(4), ListNode(5), ListNode(2), ListNode(3), ListNode(6)]
        expected = ListNode(1)
        expected.next = ListNode(2)
        expected.next.next = ListNode(3)
        expected.next.next.next = ListNode(4)
        expected.next.next.next.next = ListNode(5)
        expected.next.next.next.next.next = ListNode(6)
        solution = Solution()
        result = solution.mergeKLists(lists)
        self.assertEqual(result.val, expected.val)
        self.assertEqual(result.next.val, expected.next.val)
        self.assertEqual(result.next.next.val, expected.next.next.val)
        self.assertEqual(result.next.next.next.val, expected.next.next.next.val)
        self.assertEqual(result.next.next.next.next.val, expected.next.next.next.next.val)
        self.assertEqual(result.next.next.next.next.next.val, expected.next.next.next.next.next.val)
        self.assertIsNone(result.next.next.next.next.next.next)

if __name__ == '__main__':
    unittest.main()