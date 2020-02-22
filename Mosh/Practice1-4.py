message = """Mosh's questions on Primitive Types, Control Flow & Functions:
(https://programmingwithmosh.com/python/python-exercises-and-questions-for-beginners/)
"""
print(message)
name = "john smith"
print(name[1])
print(name[-2])
print(name[1:-1])
print(len(name))
result = f"{2 + 2} + {10 % 3}"  # Notice!
print(result)
print(name.title())
print(name.strip())
print(name.find("mith"))   # Returns the index
print(name.replace("j", "k"))   # Replace j with k. Note it's case sensitive
print("john" in name)
print(round(3.587))
# “bag” > “apple” # Boolean would be True - See ord("b"), ord("a")
# Under what circumstances does the expression:
# 18 <= age < 65 evaluate to True?
age = 66
message_two = True
if 18 <= age < 65:
    print(message_two)
else:
    print(not(message_two))
# Iterable Obj in Python:
# String (Eg.: "Blahbla, bla"),
# Lists (Eg.: [1, 2, 3, etc]),
# Range obj (eg.: range(5)),
# Custom obj (Eg.: shopping_list )

message_2 = """ 
--Mosh's Coding Exercises--

"""
print(message_2)
# -1 Write a function that returns the maximum of two numbers.


def maximum(num_1, num_2):
    if num_1 > num_2:
        return num_1
    else:
        return num_2


print(maximum(20, 8))
#
print("")
print("")

# -2 Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):   # The () are not necessary but code looks more readable
        return "FizzBuzz"  # Don't need to create a 'result' variable. We can return a string directly and eliminate a line of code!
    if input % 3 == 0:    # Don't need elif 'cause we return a value and if the previous if is false the code skips to the next step anyway
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input     # The indentetion for return allows us to skip else: because the previous ifs are all false


print(fizz_buzz(15))
###
print("")
print("")
# -3 Write a function for checking the speed of drivers.
#  This function should have one parameter: speed.

# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit(70),
# it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points,
# the function should print: “License suspended”


def check_speed(speed):
    limit = 70
    points = 0
    if speed <= limit:
        print("Ok")
    else:
        for i in range(limit, speed, 5):
            points += 1
        if points > 12:
            print("License suspended")
        else:
            print("Points:", points)


check_speed(110)
#
print("")
print("")
# -4 Write a function called showNumbers that takes a parameter called limit.
# It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
# For example, if the limit is 3, it should print:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD


def showNumbers(limit):
    for i in range(-1, limit):
        i += 1
        if i % 2 == 0:
            print(i, "EVEN")
        else:
            print(i, "ODD")


showNumbers(10)


print("")
print("")
# -5 Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
# For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.


def show_sum(limit):
    total = 0
    for i in range(limit):
        i += 1
        if i % 3 == 0 or (i % 5 == 0):
            total += i
        else:
            pass
    print(total)


show_sum(20)

print("")
print("")
# -6 Write a function called show_stars(rows).
# If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****


def show_stars(rows):
    for stars in range(rows):
        stars += 1
        print(stars * "*")


show_stars(5)

print("")
print("")
# -7 Write a function that prints all the prime numbers
# between 0 and limit where limit is a parameter.


print("")
print("")
# - EXTRA PRACTICE -
# -8 Write a function that returns age
# based on two parameters, current year and birth year


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


my_age = calculate_age(2049, 1993)
dads_age = calculate_age(2049, 1953)
print("I am", str(my_age), "years old and my dad is", str(dads_age), "years old")

print("")
print("")
# -9 Multiple Return Values.


def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = target + margin
    return low_limit, high_limit


low, high = get_boundaries(100, 20)
print(low)
print(high)

print("")
print("")
# -10 CHECK THIS


def repeat_stuff(stuff, num_repeats=10):
    return stuff * num_repeats


repeat_stuff("Row ", 3)
lyrics = repeat_stuff("Row ", 3) + "Your Boat. "
song = repeat_stuff(lyrics)
print(song)
