import unittest
from POAI import Solution
class test_POAI(unittest.TestCase):
    def test_POAI(self):
        # Test case 1
        nums1 = [1,2,3,4]
        expected1 = [24,12,8,6]
        self.assertEqual(Solution.poai(self, nums1), expected1)

        # Test case 2
        nums2 = [1,2,3,4,5]
        expected2 = [120,60,40,30,24]
        self.assertEqual(Solution.poai(self, nums2), expected2)

        # Test case 3
        nums3 = [1,2]
        expected3 = [2,1]
        self.assertEqual(Solution.poai(self, nums3), expected3)

if __name__ == '__main__': 
    unittest.main()