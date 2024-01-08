import unittest
from LCS import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        nums = [100, 4, 200, 1, 3, 2]
        sol = Solution()
        self.assertEqual(sol.longestConsecutive(nums), 4)

    def test2(self):
        nums = [100, 4, 200, 1, 3, 2, 5]
        sol = Solution()
        self.assertEqual(sol.longestConsecutive(nums), 5)

    def test3(self):
        nums = [100, 4, 200, 1, 3, 2, 5, 6]
        sol = Solution()
        self.assertEqual(sol.longestConsecutive(nums), 6)

    def test4(self):
        nums = [100, 4, 200, 1, 3, 2, 5, 6, 7]
        sol = Solution()
        self.assertEqual(sol.longestConsecutive(nums), 7)

    def test5(self):
        nums = [100, 4, 200, 1, 3, 2, 5, 6, 7, 8]
        sol = Solution()
        self.assertEqual(sol.longestConsecutive(nums), 8)

    def test6(self):
        nums = [100, 4, 200, 1, 3, 2, 5, 6, 7, 8, 9]
        sol = Solution()
        self.assertEqual(sol.longestConsecutive(nums), 9)

    def test7(self):
        nums = [100, 4, 200, 1, 3, 2, 5, 6, 7, 8, 9, 10]
        sol = Solution()
        self.assertEqual(sol.longestConsecutive(nums), 10)

    def test8(self):
        nums = [100, 4, 200, 1, 3, 2, 5, 6, 7, 8, 9, 10, 11]
        sol = Solution()
        self.assertEqual(sol.longestConsecutive(nums), 11)

    def test9(self):
        nums = [100, 4, 200, 1, 3, 2, 5, 6, 7, 8, 9, 10, 11, -1]
        sol = Solution()
        self.assertEqual(sol.longestConsecutive(nums), 11)

    def test10(self):
        nums = [100, 4, 200, 1, 3, 2, 5, 6, 7, 8, 9, -1, 10, 11]
        sol = Solution()
        self.assertEqual(sol.longestConsecutive(nums), 11)

if __name__ == '__main__':
    unittest.main()