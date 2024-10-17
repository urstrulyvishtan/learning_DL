class Solution:
    def myPow(self, x: float, n: int) -> float: 
        if n == 0: 
            return 1
        if n == 1:
            return x
        if n<0:
            x = 1/x
            n = -n
        half = self.myPow(x, n//2)

        if n%2 == 0:
            return half*half
        else:
            return half*half*x

# n = 0 return 1 
# n = 1 return x 
# n is negative 1/x^n
# if n is even, we compute x^n  by squaring x^n/2
# if n is odd we compute x^n as x times x^n-1 reduce the problem.

# x = 2, n = 10
# mypow(2, 5) -> myPow(2, 2) -> myPow(2,1)
# myPow(2,2) -> 2*2 = 4
# my(2, 5) -> 4*4*2=32
# myPow(2, 10) -> 32*32 = 1024

# time complexity O(log n)
# space complexity O(long n)