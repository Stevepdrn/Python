### Lists ###
message = """1- Lists:
"""
print(message)
# Use [] to define a list or a sequence of obj. of any type (strings, numbers, booleans or other lists(see matrix below))
letters = ["a", "b", "c"]

matrix = [[0, 1], [1, 2]]  # it's a 2 dimensional list
zeros = [0] * 5
combined = zeros + letters  # Every obj in a list can be of different type

# - Below, the list() function takes an iterable ( here a 'range' function taking an iterable obj '20') and convert it into a list
numbers = list(range(20))  # NOTE!!!
chars = list("Hello World")  # Strings are also iterable
# - print(len(chars)) -# Using 'len' function to get the number of items in the chars list
#   Try print defined variables above


### Accessing Items ###
message = """2- Accessing Items:
"""
print(message)
letters = ["a", "b", "c", "d"]
# Below, use [] to access individual items in 'letters' list
print(letters[0])  # returns firts item on the list
print(letters[-1])  # returns last item
letters[0] = "A"  # Use [] to modify items in the list
print(letters)
print(letters[0:3])  # Use two indexes between [] to slice a string
# See variable 'numbers' above then try:
# The :: would print all the numbers from 0 to 19 but with added 2 it prints every other numb
print(numbers[::2])
print(letters[::2])  # Returns ['A', 'c'] !!!
print(numbers[::-1])  # Returns all numb in list but in reverse order

print("")
### Unpacking Lists ###
message = """3- List Unpacking:
"""
print(message)

# # To get individual itmes in a list and assign the to different variables
numbers = [1, 2, 3, 3, 4]
# first = numbers[0]
# sencond = numbers[1]
# third = numbers[2]
# # A better way to do this is through lists unpacking:
# Numb. of variables on the left of =should be equal to numb. of items in the list!
first, second, third, fourth, fifth = numbers
first, second, *other = numbers
print(first)  # Prints 1
print(other)  # Print a list of all items after 2 i.e: [3, 3, 4]
# # As saw in Functions, when we prefix a parameter with *
# # Python gets all the arbitrary arguments and pack them into a list
first, *other, last = numbers
print(first, last)  # Returns first & last items (here numb.1 & 9)
print(other)  # Returns a list containing all the other numb.

print("")
### Looping over Lists ###
message = """4- Looping over Lists:
"""

print(message)
letters = ["a", "b", "c"]
for letter in letters:
    print(letter)
# Below, each enumerate obj (i.e. each iteration)
# will give us a tuple (It's like a list but it's READ ONLY):
for letter in enumerate(letters):
    print(letter)
# So each iteration gives a tuple (0, "a") of 2 items.
# The first item is the index and the second is the item in that index!!!
# Next, using list unpacking:

# Say we have a list with 2 items [0, "a"] and change [] to () to have tuple
items = (0, "a")
# then we can unpack the tuple into 2 variables (index letter)
index, letter = items
# Add the index variable to previous for loop
for index, letter in enumerate(letters):
    print(index, letter)

print("")
### Adding or Removing Items ###
message = """5- Adding or Removing Items:
"""
print(message)
# Add to a list i.e. letters
## !!! When A function is part of an obj we refer to that function as a METHOD ##
# Here's the 'dot' . notation to access individual methods of that obj
letters.append("e")  # append method adds item at the end of a list
letters.insert(0, "-")  # to add at a specific position
print(letters)
# Remove
letters.pop()  # to remove item at the end
print(letters)

letters.pop(0)  # the index 0 removes the first item
print(letters)

letters.remove("b")  # to remove item when the index is unknown
print(letters)

del letters[0:3]  # removes a range of items
print(letters)

# !!! letters.clear() # removes all the obj on that list
print("")
### Finding objects in a list ###
message = """6- Finding Items:
"""
print(message)

letters = ["a", "b", "c"]
print(letters.count("b"))

if "a" in letters:   # If letter not in list it doesn't return an error (try d)
    print(letters.index("a"))

print("")
### Sorting lists ###
message = """7- Sorting items:
"""
print(message)

numbers = [3, 42, 6, 1, 8, 2, 5]
# numbers.sort()
# print(numbers)
print(sorted(numbers))  # Same results as the 2 lines above
# numbers.sort(reverse=True)
# print(numbers)
print(sorted(numbers, reverse=True))  # Same results as the 2 lines above

# -- Custom Sorting:

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 11)
]   # Note: each item is a tuples.
# so if we wnat to sort each item by the number
# following, we need to create a function:


# def sort_item(item):
#     return item[1]


# item.sort(key=sort_item)
# print(items)
print("")
### Lambda Functions ###
# are anonimous functions

message = """8- Lambda Functions:
"""
print(message)
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 11)
]
# we define a lambda function by using this syntax: lambda parameters: expression
items.sort(key=lambda item: item[1])
print(items)
