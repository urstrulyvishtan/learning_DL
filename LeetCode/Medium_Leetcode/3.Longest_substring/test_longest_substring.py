import unittest
from longest_substring import Solution

class TestLengthOfLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_lengthOfLongestSubstring(self):
        # Test case with unique characters
        s = "abcde"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 5)

        # Test case with repeated characters
        s = "aabbc"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 2)

        # Test case with empty string
        s = ""
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 0)

        # Test case with all same characters
        s = "aaaaa"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 1)

        # Test case with mix of unique and repeated characters
        s = "abccba"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 3)

if __name__ == '__main__':
    unittest.main()