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


# Part 6


# Part 7


# Part 8


