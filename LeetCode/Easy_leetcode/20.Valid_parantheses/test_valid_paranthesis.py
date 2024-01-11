import unittest
from valid_paranthesis import Solution

class TestValidParanthesis(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_paranthesis(self):
        # Test case with valid parentheses
        self.assertTrue(self.solution.valid_paranthesis("()"))
        self.assertTrue(self.solution.valid_paranthesis("()[]{}"))
        self.assertTrue(self.solution.valid_paranthesis("{[]}"))
        self.assertTrue(self.solution.valid_paranthesis("[{()}]"))

        # Test case with invalid parentheses
        self.assertFalse(self.solution.valid_paranthesis("("))
        self.assertFalse(self.solution.valid_paranthesis(")"))
        self.assertFalse(self.solution.valid_paranthesis("([)]"))
        self.assertFalse(self.solution.valid_paranthesis("{[}]"))

        # Test case with empty string
        self.assertTrue(self.solution.valid_paranthesis(""))

if __name__ == '__main__':
    unittest.main(verbosity=2)