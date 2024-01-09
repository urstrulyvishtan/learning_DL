import unittest
from container_with_most_water import Solution

class TestContainerWithMostWater(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxArea(self):
        # Test case with increasing heights
        heights = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.maxArea(heights), 6)

        # Test case with decreasing heights
        heights = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.maxArea(heights), 6)

        # Test case with alternating heights
        heights = [1, 5, 2, 4, 3]
        self.assertEqual(self.solution.maxArea(heights), 9)

        # Test case with equal heights
        heights = [3, 3, 3, 3, 3]
        self.assertEqual(self.solution.maxArea(heights), 12)

        # Test case with empty list
        heights = []
        self.assertEqual(self.solution.maxArea(heights), 0)

        # Test case with single height
        heights = [5]
        self.assertEqual(self.solution.maxArea(heights), 0)

if __name__ == '__main__':
    unittest.main()