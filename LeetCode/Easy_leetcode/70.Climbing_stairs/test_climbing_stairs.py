import unittest
from climbing_stairs import Solution

class TestClimbingStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_ClimbStairs(self):
        # Test case 1
        n = 2
        expected = 2
        self.assertEqual(self.solution.ClimbStairs(n), expected)

        # Test case 2
        n = 3
        expected = 3
        self.assertEqual(self.solution.ClimbStairs(n), expected)

        # Test case 3
        n = 4
        expected = 5
        self.assertEqual(self.solution.ClimbStairs(n), expected)

        # Test case 4
        n = 5
        expected = 8
        self.assertEqual(self.solution.ClimbStairs(n), expected)

if __name__ == '__main__':
    unittest.main()