import unittest
from encode_decode import Solution

class TestSolution(unittest.TestCase):
    def Testcases(self):
        s = Solution()
        # Test case 1
        self.assertEqual(s.encode(["hello", "world"]), "5#/hello5#/world")
        self.assertEqual(s.decode("5#/hello5#/world"), ["hello", "world"])

        # Test case 2
        self.assertEqual(s.encode([""]), "0#//")
        self.assertEqual(s.decode("0#//"), [""])

        # Test case 3
        self.assertEqual(s.encode([]), "")
        self.assertEqual(s.decode(""), [])

        # Test case 4
        self.assertEqual(s.encode(["a"]), "1#/a")
        self.assertEqual(s.decode("1#/a"), ["a"])

if __name__ == "__main__":
    unittest.main()