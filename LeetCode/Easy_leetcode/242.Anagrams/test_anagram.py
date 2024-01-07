import unittest
from anagram import Solution

class TestSolution(unittest.TestCase):
    def test_anagramSorted(self):
        # Test case 1
        s1 = "anagram"
        t1 = "nagaram"
        expected1 = True
        self.assertEqual(Solution.anagramSorted(s1, t1), expected1)

        # Test case 2
        s2 = "rat"
        t2 = "car"
        expected2 = False
        self.assertEqual(Solution.anagramSorted(s2, t2), expected2)

    def test_anagramHash(self):
        # Test case 1
        s1 = "anagram"
        t1 = "nagaram"
        expected1 = True
        self.assertEqual(Solution.AnagramHash(s1, t1), expected1)

        # Test case 2
        s2 = "rat"
        t2 = "car"
        expected2 = False
        self.assertEqual(Solution.AnagramHash(s2, t2), expected2)

if __name__ == '__main__':  
    unittest.main()