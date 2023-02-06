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
    def test_short_lists(self):
        input = [[1,2],[3,4,5],[6],[7,8]]
        result = hw1.short_lists(input)
        expected = [1,2,7,8]
        self.assertEqual(expected,result)

    def test_short_lists_none(self):
        input = [[3,1,2],[1], ["hello"], ["a", "b", "c"]]
        result = hw1.short_lists(input)
        expected = []
        self.assertEqual(expected, result)

    # Part 3
    def test_ascending_pairs(self):
        input = [[1,2],[2,1],[3,2,1]]
        result = hw1.ascending_pairs(input)
        expected = [[1,2],[1,2],[3,2,1]]
        self.assertEqual(expected, result)

    def test_ascending_pairs_reverse(self):
        input = [[2,1],[3,2],[4,3],[5,4]]
        result = hw1.ascending_pairs(input)
        expected = [[1,2],[2,3],[3,4],[4,5]]
        self.assertEqual(expected,result)

    def test_ascending_pairs_extra(self):
        input = [[5,4], [4,1,5,6], [7,1,2], [9,8]]
        result = hw1.ascending_pairs(input)
        expected = [[4,5], [4,1,5,6], [7,1,2], [8,9]]
        self.assertEqual(expected,result)

    # Part 4


    # Part 5


    # Part 6


    # Part 7


    # Part 8





if __name__ == '__main__':
    unittest.main()
