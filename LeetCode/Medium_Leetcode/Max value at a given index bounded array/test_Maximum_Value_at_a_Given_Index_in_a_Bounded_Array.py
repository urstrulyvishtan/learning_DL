import unittest
from Maximum_Value_at_a_Given_Index_in_a_Bounded_Array import Solution

class TestSolution(unittest.TestCase):
    def test_maxValue(self):
        # Test case 1
        n1 = 4
        index1 = 2
        max_sum1 = 6
        expected1 = 2
        self.assertEqual(Solution.maxValue(n1, index1, max_sum1), expected1)

        # Test case 2
        n2 = 6
        index2 = 1
        max_sum2 = 10
        expected2 = 3
        self.assertEqual(Solution.maxValue(n2, index2, max_sum2), expected2)

        # Test case 3
        n3 = 10
        index3 = 5
        max_sum3 = 30
        expected3 = 4
        self.assertEqual(Solution.maxValue(n3, index3, max_sum3), expected3)

if __name__ == '__main__':
    unittest.main()