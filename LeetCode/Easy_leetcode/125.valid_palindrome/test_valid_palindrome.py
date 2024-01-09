import unittest
from valid_palindrome import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        sol = Solution()
        s = "A man, a plan, a canal: Panama"
        self.assertTrue(sol.isPalindrome(s))

    def test2(self):
        sol = Solution()
        s = "race a car"
        self.assertFalse(sol.isPalindrome(s))

    def test3(self):
        sol = Solution()
        s = "level"
        self.assertTrue(sol.isPalindrome(s))

    def test4(self):
        sol = Solution()
        s = "12321"
        self.assertTrue(sol.isPalindrome(s))

    def test5(self):
        sol = Solution()
        s = "hello"
        self.assertFalse(sol.isPalindrome(s))

if __name__ == '__main__':
    unittest.main()