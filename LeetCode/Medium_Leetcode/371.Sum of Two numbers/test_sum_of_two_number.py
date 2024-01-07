import unittest
from sum_of_two_number import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_getSums_positive_numbers(self):
        result = self.solution.getSums(5, 7)
        self.assertEqual(result, 12)

    def test_getSums_negative_numbers(self):
        result = self.solution.getSums(-5, -7)
        self.assertEqual(result, -12)

    def test_getSums_mixed_numbers(self):
        result = self.solution.getSums(-5, 7)
        self.assertEqual(result, 2)

    def test_getSums_zero(self):
        result = self.solution.getSums(0, 0)
        self.assertEqual(result, 0)

    def test_getSums_large_numbers(self):
        result = self.solution.getSums(123456789, 987654321)
        self.assertEqual(result, 1111111110)

if __name__ == '__main__':
    unittest.main()