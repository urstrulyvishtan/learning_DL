import unittest
from house_robber import Solution
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_rob_empty_list(self):
        nums = []
        expected = 0
        self.assertEqual(self.solution.rob(nums), expected)

    def test_rob_single_house(self):
        nums = [5]
        expected = 5
        self.assertEqual(self.solution.rob(nums), expected)

    def test_rob_two_houses(self):
        nums = [2, 7]
        expected = 7
        self.assertEqual(self.solution.rob(nums), expected)

    def test_rob_multiple_houses(self):
        nums = [1, 2, 3, 1]
        expected = 4
        self.assertEqual(self.solution.rob(nums), expected)

    def test_rob_large_houses(self):
        nums = [1, 2, 3, 1, 5, 6, 7, 8, 9, 10]
        expected = 28
        self.assertEqual(self.solution.rob(nums), expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)