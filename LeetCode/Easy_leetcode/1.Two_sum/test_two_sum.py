import unittest
from two_sum import Solution
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_twoSum(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        self.assertEqual(self.solution.twoSum(nums, target), expected)

        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        self.assertEqual(self.solution.twoSum(nums, target), expected)

        nums = [3, 3]
        target = 6
        expected = [0, 1]
        self.assertEqual(self.solution.twoSum(nums, target), expected)

if __name__ == '__main__':
    unittest.main()