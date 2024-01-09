import unittest
from threeSum import Solution
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sum_empty_list(self):
        nums = []
        expected = []
        self.assertEqual(self.solution.Sum(nums), expected)

    def test_sum_no_triplets(self):
        nums = [1, 2, 3, 4, 5]
        expected = []
        self.assertEqual(self.solution.Sum(nums), expected)

    def test_sum_single_triplet(self):
        nums = [-1, 0, 1]
        expected = [[-1, 0, 1]]
        self.assertEqual(self.solution.Sum(nums), expected)

    def test_sum_multiple_triplets(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(self.solution.Sum(nums), expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)