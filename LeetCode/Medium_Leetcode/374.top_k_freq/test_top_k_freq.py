import unittest
from top_k_freq import solution

class TestSolution(unittest.TestCase):
    def test_top_k_freq(self):
        
        # Test case 1
        nums1 = [1,1,1,2,2,3]
        k1 = 2
        expected1 = [1,2]
        self.assertEqual(solution.top_frequent_k(nums1, k1), expected1)

        # Test case 2
        nums2 = [1]
        k2 = 1
        expected2 = [1]
        self.assertEqual(solution.top_frequent_k(nums2, k2), expected2)

        # Test case 3
        nums3 = [1,2]
        k3 = 2
        expected3 = [1,2]
        self.assertEqual(solution.top_frequent_k(nums3, k3), expected3)

if __name__ == '__main__':
    unittest.main()
