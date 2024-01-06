import math


class Solution:
    @staticmethod
    def S(h, l):
        return (2 * h - l + 1) * l // 2

    @staticmethod
    def FindExtra(start, increment, max_sum):
        b = start * 2 // increment - 1
        c = 2 * max_sum // increment
        d = math.isqrt(b * b + 4 * c)
        n = (d - b) // 2
        return n

    @staticmethod
    def maxValue(n, index, max_sum):
        max_sum -= n
        left = index + 1
        right = n - index
        small, large = min(left, right), max(left, right)

        A = Solution.S(large, large) + Solution.S(large, small) - large
        if max_sum >= A:
            return large + (max_sum - A) // n + 1

        B = Solution.S(small, small) * 2 - small
        if max_sum >= B:
            return small + Solution.FindExtra(small * 2, 1, max_sum - B) + 1

        return Solution.FindExtra(1, 2, max_sum) + 1
    

