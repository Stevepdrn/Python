###  Comparison Operators ###
#   >, <, >=, <=, ==, !=    #

### Conditional Statements ###
temperature = 31
if temperature > 30:
    print("Dude it's hot, drink a lot of water!")
elif temperature >= 20:
    print("It's warm. Let's got out.")
else:
    print("Not so warm...let's stay in")
print("Done")
print("")
### Ternary Operator ###
# Example:
age = 16
# if age >= 18:
#    message = "Eligible"
# else:
#    message = "Not Eligible"
# print(message)
message = "Eligible" if age >= 18 else "Not Eligible"  # Using ternary operator
print(message)

### Logical Operators (and, or, not). Eg.: ###
high_income = True
good_credit = False
student = False
if (high_income or good_credit) and not student:
    print("Eligible for a loan")
else:
    print("Not Eligible")
print("")
### Chaining Comparison Operators ###
# Eg.: age should be between 18 and 65
age = 22
# if age >= 18 and age < 65:  (this is how I'd normally start)
if 18 <= age < 65:  # clearer, easier to read
    print("You're eligible!")
print("")
print("")

### For Loops ###
# Eg.:
for number in range(1, 10, 2):
    print("Attempt", number, number * ".")
print("")

### For..Else ###
successful = False  # †ry changing to True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
print("")
### Nested Loops ###
for x in range(5):
    for y in range(3):
        # notice use of 'f' see Eg. in 2primitive-types.py
        print(f"({x}, {y})")
print("")

### Iterables ###
print(type(5))  # Eg. of Primitive types, i.e. number
print(type(range(5)))  # Eg. of Complex types, i.e. range (It's Iterable)
print("")
# Eg. of iterable obj.:
# for x in "Python":  # a string
#    print(x)
# for x in [1, 2, 3]: # a list (note brackets [])
#    print(x)
# for item in shopping_cart: # using a custom obj shopping_cart
print("")

### While Loops ###

# command = ""
# while command.lower() != "quit":  # Notice: .lower() Method

# --- DON'T RUN using Code Runner in output (it's read only!!!)

#    command = input(">")
#    print("ECHO", command)  # Instead open terminal using control backtick
print("")
print("")
### EXERCISE ###
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")
