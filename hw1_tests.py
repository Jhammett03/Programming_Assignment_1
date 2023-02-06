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
    def test_add_prices(self):
        input1 = data.Price(3,99)
        input2 = data.Price(1,99)
        result = hw1.add_prices(input1, input2)
        expected = data.Price(5,98)
        self.assertEqual(expected, result)

    def test_add_prices_2(self):
        input1 = data.Price(3,50)
        input2 = data.Price(1,5)
        result = hw1.add_prices(input1, input2)
        expected = data.Price(4,55)
        self.assertEqual(expected, result)
    # Part 5
    def test_rectangle_area(self):
        input = data.Rectangle(data.Point(0,10), data.Point(10,0))
        result = hw1.rectangle_area(input)
        expected = 100
        self.assertEqual(expected, result)

    def test_negative_rectangle_area(self):
        input = data.Rectangle(data.Point(-5,2), data.Point(5,-8))
        result = hw1.rectangle_area(input)
        expected = 100
        self.assertEqual(expected, result)

    # Part 6
    def test_books_by_author(self):
        input1 = "Charles Dickens"
        input2 = [data.Book(["Charles Dickens"], "A Tale of Two Cities"), data.Book(["John Steinbeck"], "Of Mice and Men"), data.Book(["Charles Dickens"], "A Christmas Carol")]
        result = hw1.books_by_author(input1, input2)
        expected = [data.Book(["Charles Dickens"], "A Tale of Two Cities"), data.Book(["Charles Dickens"], "A Christmas Carol")]
        self.assertEqual(expected, result)

    def test_books_by_author_multiple_authors(self):
        input1 = "Joe Mama"
        input2 = [data.Book(["Jared Hammett","Joe Mama"], "Book A"), data.Book(["Obama"], "Book B"), data.Book(["Author A", "Author B", "Joe Mama"], "Book C")]
        result = hw1.books_by_author(input1, input2)
        expected = [data.Book(["Jared Hammett", "Joe Mama"], "Book A"), data.Book(["Author A", "Author B", "Joe Mama"], "Book C")]
        self.assertEqual(expected, result)
    # Part 7
    def test_circle_bound(self):
        input = data.Rectangle(data.Point(12,0), data.Point(0,5))
        result = hw1.circle_bound(input)
        expected = data.Circle(data.Point(6, 2.5), 13)
        self.assertEqual(expected, result)


    def test_circle_bound_negative(self):
        input = data.Rectangle(data.Point(-10, 5), data.Point(-5,17))
        result = hw1.circle_bound(input)
        expected = data.Circle(data.Point(-7.5, 11), 13)
        self.assertEqual(expected, result)


    # Part 8
    def test_below_pay_average(self):
        input = [data.Employee("Jared", 12), data.Employee("Joe", 20), data.Employee("David", 50)]
        result = hw1.below_pay_average(input)
        expected = ["Jared", "Joe"]
        self.assertEqual(expected, result)

    def test_below_pay_average_floats(self):
        input = [data.Employee("Jared", 12.5), data.Employee("Joe", 20.5), data.Employee("David", 50.5)]
        result = hw1.below_pay_average(input)
        expected = ["Jared", "Joe"]
        self.assertEqual(expected, result)




if __name__ == '__main__':
    unittest.main()
