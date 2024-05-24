## All tests will go here
import unittest
from main import add

class TestStringMethods(unittest.TestCase):
    def test_checking_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_checking_single_variable_input(self):
        self.assertEqual(add("1"), 1)

    def test_checking_multiple(self):
        self.assertEqual(add("1,5"), 6)

if __name__ == '__main__':
    unittest.main()