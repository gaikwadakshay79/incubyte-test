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

    def test_dynamic_delimiter_given_in_numbers_string_input(self):
        #  "//[delimiter]\n[numbers…]"
        self.assertEqual(add("//;1\n2;3"), 6)
        self.assertEqual(add("//k1k2\n3"), 6)
        self.assertEqual(add("//k1\n2\n3"), 6)
        self.assertEqual(add("//k1k2\n3\n4"), 10)

    def test_negative_numbers_input(self):
        with self.assertRaises(Exception) as exception:
            add("-1\n2,-3")
            self.assertEqual(exception.exception.message, 'negative numbers not allowed -1,negative numbers not allowed -3')
        with self.assertRaises(Exception) as exception:
            add("-1\n2,-3")
            self.assertEqual(exception.exception.message, 'negative numbers not allowed -2')

if __name__ == '__main__':
    unittest.main()