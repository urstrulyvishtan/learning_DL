import unittest
from find_min_in_rotated_sorted_array import Solution

class TestFindMin(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findMin(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        expected = 0
        self.assertEqual(self.solution.findMin(nums), expected)

        nums = [3, 4, 5, 1, 2]
        expected = 1
        self.assertEqual(self.solution.findMin(nums), expected)

        nums = [1]
        expected = 1
        self.assertEqual(self.solution.findMin(nums), expected)

        nums = [2, 1]
        expected = 1
        self.assertEqual(self.solution.findMin(nums), expected)

        nums = [1, 2, 3, 4, 5]
        expected = 1
        self.assertEqual(self.solution.findMin(nums), expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)