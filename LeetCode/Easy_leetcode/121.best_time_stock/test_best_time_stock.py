import unittest
from best_time_stock import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        sol = Solution()
        prices = [7,1,5,3,6,4]
        self.assertEqual(sol.maxProfit(prices), 5)

    def test2(self):
        sol = Solution()
        prices = [7,6,4,3,1]
        self.assertEqual(sol.maxProfit(prices), 0)

    def test3(self):
        sol = Solution()
        prices = [2,4,1]
        self.assertEqual(sol.maxProfit(prices), 2)

    def test4(self):
        sol = Solution()
        prices = [2,1,2,0,1]
        self.assertEqual(sol.maxProfit(prices), 1)

    def test5(self):
        sol = Solution()
        prices = [2,1,2,1,0,1,2]
        self.assertEqual(sol.maxProfit(prices), 2)

    def test6(self):
        sol = Solution()
        prices = [2,1,2,1,0,1,2,0,1,2]
        self.assertEqual(sol.maxProfit(prices), 2)

    def test7(self):
        sol = Solution()
        prices = [2,1,2,1,0,1,2,0,1,2,1,2,0,1,2]
        self.assertEqual(sol.maxProfit(prices), 2)

    def test8(self):
        sol = Solution()
        prices = [2,1,2,1,0,1,2,0,1,2,1,2,0,1,2,1,2,0,1,2]
        self.assertEqual(sol.maxProfit(prices), 2)

if __name__ == '__main__':
    unittest.main()