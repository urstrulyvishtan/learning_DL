import unittest
from Ganagrams import Solution

class TestSolution(unittest.TestCase):
    def test_groupAnagrams(self):
        solution = Solution()
        # Test case 1
        strs1 = ["eat","tea","tan","ate","nat","bat"]
        expected1 = [["bat"],["nat","tan"],["ate","eat","tea"]]
        self.assertEqual(solution.anagrams_group(strs1), expected1)

        # Test case 2
        strs2 = [""]
        expected2 = [[""]]
        self.assertEqual(solution.anagrams_group(strs2), expected2)

        # Test case 3
        strs3 = ["a"]
        expected3 = [["a"]]
        self.assertEqual(solution.anagrams_group(strs3), expected3)

if __name__ == '__main__':
    unittest.main()