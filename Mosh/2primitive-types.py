print("Hello Mofos !")
print("*" * 10)

students_count = 100
print(students_count)

message = """Hello,

This is Steve. How you doing?

Talk soon.
"""
print(message)
print(len(message))  # It includes spaces
print(message[0])  # First character is 0
print(message[2])
print(message[1:3])  # Prints characters 1 and 2

# Formatted Strings--Eg:
name = "Steve"
lucky_number = "99"
full = (name + " " + lucky_number)
print(full)
full = f"{name} {lucky_number}"  # Faster and easier way using 'f' and'{}'
print(full)
full_2 = f"{len(name)} {8 + 8}"  # Another way to use f and {}
print(full_2)

print(full.upper())     # Eg. of a method i.e .upper()
# Another method (.find) to find the index of the string ("ve") passed as an argument
print(full.find("ve"))  # Returns the index
# This expression,"ve" in full, uses the (in) operator to return a boolean as value
print("ve" in full)
print(type(full))  # It returns the type of the obj 'full' passed as an argument
