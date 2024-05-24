## All tests will go here
import unittest
from main import add

class TestStringMethods(unittest.TestCase):
    def test_checking_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_checking_single_number_string_input(self):
        self.assertEqual(add("1"), 1)

    def test_checking_two_numbers_string_input(self):
        self.assertEqual(add("1,5"), 6)

    def test_checking_multiple_numbers_string_input(self):
        self.assertEqual(add("1,2,3"), 6)
        self.assertEqual(add("1,2,3,5"), 11)

    def test_new_line_separator_between_numbers_string_input(self):
        self.assertEqual(add("1\n2,3"), 6)
        self.assertEqual(add("1,2\n3"), 6)
        self.assertEqual(add("1\n2\n3"), 6)
        self.assertEqual(add("1,2\n3\n4"), 10)

if __name__ == '__main__':
    unittest.main()