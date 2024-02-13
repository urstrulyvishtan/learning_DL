# Given the number of iterations to perform gradient descent, the learning rate, and an initial guess, return the value of x that globally minimizes this function.

# Round your final result to 5 decimal places using Python's round() function.
class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x = init
        for _ in range(iterations):
            x -= learning_rate * (2 * x)
        return round(x, 5)