import data
import hw1
import unittest


# Write your test cases for each part below.
class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count(self):
        input = "hello"
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(expected, result)

    def test_upper_vowel_count(self):
        input = "hEllo"
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(expected, result)

    # Part 2


    # Part 3


    # Part 4


    # Part 5


    # Part 6


    # Part 7


    # Part 8





if __name__ == '__main__':
    unittest.main()
