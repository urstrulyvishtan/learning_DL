import unittest

from smallest_kth_value_linked_list import ListNode, Solution

class TestSolution(unittest.TestCase):
    def test_KthSmallest(self):
        # Test case 1
        #       3
        #     /   \
        #    1     4
        #     \
        #      2
        root = ListNode(3,
                        ListNode(1,
                                 None,
                                 ListNode(2, None, None)),
                        ListNode(4, None, None))
        k = 1
        expected_output = 1
        self.assertEqual(Solution().KthSmallest(root, k), expected_output)

        # Test case 2
        #       5
        #     /   \
        #    3     6
        #   / \
        #  2   4
        # /
        # 1
        root = ListNode(5,
                        ListNode(3,
                                 ListNode(2,
                                          ListNode(1, None, None),
                                          None),
                                 ListNode(4, None, None)),
                        ListNode(6, None, None))
        k = 3
        expected_output = 3
        self.assertEqual(Solution().KthSmallest(root, k), expected_output)

        # Test case 3
        #       2
        #     /   \
        #    1     3
        root = ListNode(2,
                        ListNode(1, None, None),
                        ListNode(3, None, None))
        k = 2
        expected_output = 2
        self.assertEqual(Solution().KthSmallest(root, k), expected_output)

if __name__ == '__main__':
    unittest.main()