import unittest
from search_in_rotated_sorted_array import Solution

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_search(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        expected = 4
        self.assertEqual(self.solution.search(nums, target), expected)

        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        expected = -1
        self.assertEqual(self.solution.search(nums, target), expected)

        nums = [1]
        target = 1
        expected = 0
        self.assertEqual(self.solution.search(nums, target), expected)

        nums = [2, 1]
        target = 1
        expected = 1
        self.assertEqual(self.solution.search(nums, target), expected)

        nums = [1, 2, 3, 4, 5]
        target = 3
        expected = 2
        self.assertEqual(self.solution.search(nums, target), expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)