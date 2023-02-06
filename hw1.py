import math

import data

# Write your functions for each part in the space below.

# Part 1

# vowel_count function takes a string input and outputs the number of vowels that are in the word (Upper and Lower Case)
def vowel_count(word: str) -> int:
    counter = 0
    vowels = ["a","e","i","o","u"]
    for letters in word:
        if letters.lower() in vowels:
            counter += 1
    return(counter)

# Part 2

#short_lists function takes a list of a list of integers and outputs a new list of lists with exactly two indexes
def short_lists(big_list: list[list[int]]) -> list:
    new_list = []
    for small_lists in big_list:
        if len(small_lists) == 2:
            for items in small_lists:
                new_list.append(items)
    return new_list


# Part 3

# the ascending_pairs function takes a list of a list of integers and outputs the same
# list, but if a nested list has two indexes, it reorders its index values from smallest to largest
def ascending_pairs(big_list: list[list[int]]) -> list:
    new_list = []
    for small_lists in big_list:
        if len(small_lists) == 2:
            if small_lists[0] > small_lists[1]:
                temp = small_lists[0]
                small_lists[0] = small_lists[1]
                small_lists[1] = temp
        new_list.append(small_lists)
    return(new_list)

# Part 4

#The add_prices function inputs two Price objects and adds them together
# accounting for dollars and cent values and outputs them in another Price object
def add_prices(price1: data.Price, price2: data.Price) -> data.Price:
   total_cents = 100 * (price1.dollars + price2.dollars) + price1.cents + price2.cents
   total_dollars = total_cents // 100
   total_cents = total_cents % 100
   return data.Price(total_dollars, total_cents)

# Part 5

#The rectangle_area function takes a rectangle object and outputs the area of the shape
def rectangle_area(rectangle: data.Rectangle) -> float:
    x_length = rectangle.bottom_right.x - rectangle.top_left.x
    y_length = rectangle.top_left.y - rectangle.bottom_right.y
    area = x_length * y_length
    return area

# Part 6

#The books_by_author function takes a string input of the desired author, as well as a list of Book onjects and
#outputs a list of Book objects which are either written or cowritten by the desired author
def books_by_author(author: str, book_list: list[data.Book]) -> list[data.Book]:
    new_list = []
    for books in book_list:
        for names in books.authors:
            if names == author:
                new_list.append(books)
    return new_list


# Part 7

#The circle_bound function creates a bounding circle based on a given rectangle object input. The function takes the
# corner points of the rectangle and calculates the center point and radius to one of the rectangles
# corners and outputs a Circle object
def circle_bound(rect: data.Rectangle) -> data.Circle:
    width = rect.bottom_right.x - rect.top_left.x
    height = rect. bottom_right.y - rect.top_left.y
    center = data.Point(rect.top_left.x + width / 2, rect.bottom_right.y - height / 2)
    radius = math.sqrt((width) ** 2 + (height) **2)
    return data.Circle(center, radius)

# Part 8

#The below_pay_average function takes a list of Employee objects and calculates the average of their pay rates, then
#creates a new list of names of the employees who earn less than the average payrate.
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    total_pay = 0
    below_average = []
    for people in employees:
        total_pay += people.pay_rate
    average_pay = total_pay / len(employees)
    for people in employees:
        if people.pay_rate < average_pay:
            below_average.append(people.name)
    return below_average

