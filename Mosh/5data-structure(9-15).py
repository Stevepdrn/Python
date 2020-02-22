### Lists  From Codecademy ###
from sys import getsizeof
from collections import deque
message = """Lists eg. from Codecademy:
"""
print(message)
first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']
age = []
age.append(42)
print(age)
all_ages = age + [32, 41, 29]
print(all_ages)
name_and_age = list(zip(first_names, all_ages))

print(name_and_age)

print("")
print("")

last_semester_gradebook = [
    ("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

subjects.append("computer science")
grades.append(100)

gradebook = list(zip(subjects, grades))

gradebook.append(("visual arts", 93))  # notice the (( ))
print(gradebook)

full_gradebook = (last_semester_gradebook + gradebook)
print(full_gradebook)

### Map Function ###
message = """ 9- Map Function:

"""
print(message)
# map function takes a lambda function and applies it to an iterable

items = [       # each item on this list is tuple of 2 items
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 11)
]           # say we want to change it to show just the prices

prices = []     # define empty list
for item in items:  # use a loop to iterate over each item
    prices.append(item[1])  # returns the price of each item

print(prices)
print("")
print("")
# a better way to achieve the same is to use the map function:

# here we convert it into a list obj
prices = list(map(lambda item: item[1], items))
print(prices)

print("")

### Filter Function ###
message = """ 10- Filter Function:

"""
print(message)
# Next, we want to filter the list and get a price > 10:
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 11)
]

x = filter(lambda item: item[1] >= 10, items)
# this prints a filtered obj which is iterable (like in map function)so we can convert it into a list.
print(x)
# Here's the list:
filtered_list = list(filter(lambda item: item[1] >= 10, items))
print(filtered_list)
print("")
print("")


### 11- List Comprehension ###
# NOTICE !!! It's the preferred way to Map and Filter lists in Python
message = """ 11- List Comprehension:

"""
print(message)

# Eg. of mapping previous list
prices = [item[1] for item in items]
print(prices)

# Eg. of filtering previous list
filtered_list = [item for item in items if item[1] >= 10]
print(filtered_list)

print("")
print("")

### 12- Zip Function ###
# Used to combine different lists!
message = """ 12- Zip Function:

"""
print(message)
# See also Eg. from Codecademy above
# Eg.:
list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip("abc", list1, list2)))

print("")
print("")

### 13- Stacks ###
# LIFO (last in - first out)
message = """ 13- Stacks:

"""
print(message)

# Eg. of how a browser keeps track of visited sites:

browsing_session = []
browsing_session.append(1)  # .append method to add item on top of the stack
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()  # to remove item
print(last)
print(browsing_session)
print("redirect", browsing_session)
if not browsing_session:  # to check if our stack is empty or not
    browsing_session[-1]    # index -1 to get item on top of the stack
    print("disable")

print("")
print("")

### 14- Queues ###
# FIFO (first in - first out)
message = """ 14- Queues:

"""
print(message)
# First we write the line below which when saved and executed it's gonna disappear:
# from collections import deque (collections is a Module and deque is a Class)

# we wrap following list with a deque obj and pass an empty list [] as an argument.
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()  # to remove an item from the beginning of the queue (check output)
print(queue)
if not queue:
    print("empty")

print("")
print("")

### 15- Tuples ###
#
message = """ 15- Tuples:

"""
print(message)
#
# It's a read only list. () are used but not needed, see below
point = 1, 2
print(type(point))
# Tuples can be concatenated, using +, or repeated using *.
point = (1, 2) + (3, 4)
print(point)

point = (1, 2) * 3
print(point)

point = tuple([1, 2, 3])  # convert a list into a tuple
print(point)

point = tuple("Hello Me")  # or a string
print(point)

point = (1, 2, 3, 4)
print(point[0:2])  # to access individual items using an index

print("")
print("")

### 16- Swapping Variables ###

message = """ 16- Swapping Variables:

"""
print(message)

# cool trick:
x = 10
y = 5
print(x, y)
x, y = y, x  # this swaps the variables x and y in 1 line of code
print(x, y)

print()
message = """ 17- Arrays:

"""
print(message)

print()
message = """ 18- Sets:

"""
# An unordered collection of unit items, can't be indexed.
print(message)


numbers = [1, 1, 3, 4, 4, 5]
uniques = set(numbers)
print(uniques)
print()

first = set(numbers)
second = {1, 4, 6}
print(first | second)  # items either in one or the other
print(first & second)  # only numb that exist in both sets
print(first - second)  # remaining numb
print(first ^ second)  # either one or other but not both


print()
message = """ 19- Dictionaries:

"""
print(message)
# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601,
#                     "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
building_heights = dict(BurjKhalifa=828, ShanghaiTower=632, AbrajAlBait=601,
                        PingAn=599, LotteWorldTower=554.5, OneWorldTrade=541.3)

print(building_heights)

# point = {"x": 1, "y": 2}  Instead we use dict() SIMPLER!
point = dict(x=1, y=2)
print(point["x"])
print(point)


print()
message = """ 20- Dictionaries Comprehension:

"""
print(message)

# firts a List comprehension example:
value = []
for x in range(5):
    value.append(x * 2)
# can be done in just one line:
value = [x * 2 for x in range(5)]
print(value)

# or we can have a Set:
value = {x * 2 for x in range(5)}
print(value)

# or a Dictionary with key: value pairs!!!:
value = {x: x * 2 for x in range(5)}
print(value)

# Tuple ?
value = (x * 2 for x in range(5))
print(value)  # we get a Generator object. See next

print()
message = """ 21- Generator Expressions:

"""
print(message)


# generator object. More efficent when dealing with very large numbers
values = (x * 2 for x in range(10))
print(values)
for x in values:  # because G.O. are iterable they can print a value for each iteration
    print(x)


print()
message = """ 22- Unpacking Operators:

"""
print(message)

# Example:
numbers = [1, 2, 3]
print(numbers)
print(*numbers)  # use * to unpack and print individual items
print()
# We can use * to unpack items and put them into a list:
# values = list(range(5))
# same as var. above and we can use it for strings
values = [*range(5), *"Hello!"]
print(values)
print()

# NOTE We can unpack and combine dictonaries with ** :
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**second, **first, "z": 3}
print(combined)  # the last value we'll be used so 1 for x.


print()
message = """ 23- Exercise:

"""
print(message)

sentence = "This is a common interview question"
# find the most repeated character in sentence

char_frequency = {}  # use empty dictionary to create a key/value pair

for char in sentence:   # to iterate over the string
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)

print(char_frequency_sorted[0])
