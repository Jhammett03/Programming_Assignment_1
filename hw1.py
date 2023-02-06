import math

import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(word: str) -> int:
    counter = 0
    vowels = ["a","e","i","o","u"]
    for letters in word:
        if letters.lower() in vowels:
            counter += 1
    return(counter)

# Part 2
def short_lists(big_list: list[list[int]]) -> list:
    new_list = []
    for small_lists in big_list:
        if len(small_lists) == 2:
            for items in small_lists:
                new_list.append(items)
    return new_list


# Part 3
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
def add_prices(price1: data.Price, price2: data.Price) -> data.Price:
   total_cents = 100 * (price1.dollars + price2.dollars) + price1.cents + price2.cents
   total_dollars = total_cents // 100
   total_cents = total_cents % 100
   return data.Price(total_dollars, total_cents)

# Part 5
def rectangle_area(rectangle: data.Rectangle) -> float:
    x_length = rectangle.bottom_right.x - rectangle.top_left.x
    y_length = rectangle.top_left.y - rectangle.bottom_right.y
    area = x_length * y_length
    return area

# Part 6
def books_by_author(author: str, book_list: list[data.Book]) -> list[data.Book]:
    new_list = []
    for books in book_list:
        for names in books.authors:
            if names == author:
                new_list.append(books)
    return new_list


# Part 7
def circle_bound(rect: data.Rectangle) -> data.Circle:
    width = rect.bottom_right.x - rect.top_left.x
    height = rect. bottom_right.y - rect.top_left.y
    center = data.Point(rect.top_left.x + width / 2, rect.bottom_right.y - height / 2)
    radius = math.sqrt((width) ** 2 + (height) **2)
    return data.Circle(center, radius)

# Part 8


