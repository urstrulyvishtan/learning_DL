import unittest
from duplicate import Solution

class TestSolution(unittest.TestCase):
    def test_duplicate(self):
        # Test case 1
        nums1 = [1, 2, 3, 1]
        expected1 = True
        self.assertEqual(Solution().duplicate(nums1), expected1)

        # Test case 2
        nums2 = [1, 2, 3, 4]
        expected2 = False
        self.assertEqual(Solution().duplicate(nums2), expected2)

        # Test case 3
        nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        expected3 = True
        self.assertEqual(Solution().duplicate(nums3), expected3)

if __name__ == '__main__':
    unittest.main()