import unittest
from linked_list_cycle import ListNode, Solution

class TestLinkedListCycle(unittest.TestCase):
    def test_hasCycle(self):
        # Test case 1: Empty list
        head = None
        expected = False
        solution = Solution()
        result = solution.hasCycle(head)
        self.assertEqual(result, expected)

        # Test case 2: List with only one node
        head = ListNode(1)
        expected = False
        solution = Solution()
        result = solution.hasCycle(head)
        self.assertEqual(result, expected)

        # Test case 3: List with two nodes, no cycle
        head = ListNode(1)
        head.next = ListNode(2)
        expected = False
        solution = Solution()
        result = solution.hasCycle(head)
        self.assertEqual(result, expected)

        # Test case 4: List with two nodes, cycle
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = head
        expected = True
        solution = Solution()
        result = solution.hasCycle(head)
        self.assertEqual(result, expected)

        # Test case 5: List with multiple nodes, no cycle
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        expected = False
        solution = Solution()
        result = solution.hasCycle(head)
        self.assertEqual(result, expected)

        # Test case 6: List with multiple nodes, cycle
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = head.next
        expected = True
        solution = Solution()
        result = solution.hasCycle(head)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()