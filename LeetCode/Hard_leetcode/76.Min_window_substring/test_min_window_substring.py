import unittest
from min_window_substring import Solution

class TestMinWindowSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minWindow(self):
        # Test case 1
        s1 = "ADOBECODEBANC"
        t1 = "ABC"
        expected1 = "BANC"
        self.assertEqual(self.solution.minWindow(s1, t1), expected1)

        # Test case 2
        s2 = "a"
        t2 = "a"
        expected2 = "a"
        self.assertEqual(self.solution.minWindow(s2, t2), expected2)

        # Test case 3
        s3 = "a"
        t3 = "b"
        expected3 = ""
        self.assertEqual(self.solution.minWindow(s3, t3), expected3)

        # Test case 4
        s4 = "aa"
        t4 = "aa"
        expected4 = "aa"
        self.assertEqual(self.solution.minWindow(s4, t4), expected4)

        # Test case 5
        s5 = "cabwefgewcwaefgcf"
        t5 = "cae"
        expected5 = "cwae"
        self.assertEqual(self.solution.minWindow(s5, t5), expected5)

if __name__ == '__main__':
    unittest.main(verbosity=2)