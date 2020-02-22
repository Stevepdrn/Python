### Defining Functions + Arguments###
def greet(first_name, last_name):  # In parethesis we have 2 Parameters
    # f converts to formatted string. After Hi we pass 2 fields using{}
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Steve", "Pedron")  # In parenthesis are 2 Arguments
greet("Joe", "Diaz")
print("")
print("")
### Types of Functions ###
# 1- Perform a task, see eg. above
# 2- Return a value, eg. round(1.9) or see below


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Steve")
print(message)
# The message variable above can be reused eg.: print it to terminal, write in a file, send it via email...
print("")
print("")
### Keyword Arguments ###


def increment(number, by):
    return number + by


print(increment(2, 1))  # Here's Not clear what the arguments 2 & 1 are for
print(increment(2, by=1))  # More readable as we use the keyword argument by=1
print("")
print("")
### Default Arguments ###


# The 2nd parameter has a default value of 1 and it's an optional parameter
def increment_2(number, by=1):
    # Optional parameters should come after the required parameters, here is number
    return number + by


# Below we removed the second argument 1.
# If we pass a second argument after 2 eg.: (2, 5) it increments number by 5 instead of 1
print(increment_2(2))
print("")
print("")

### Xargs & XXargs ###


def multiply(*numbers):  # we prefix the single parameter with * to make a Tuples
    total = 1
    for number in numbers:  # The loop iterates the tuples in the parameter below
        # print(numbers) # This would print the tuples (list of arguments 2, 3, 4, 5)
        total *= number  # Same as total = total * number, but cleaner!
    return total  # Notice indentation!


print(multiply(2, 3, 4, 5))  # Here's the arguments for the parameter 'numbers'

print("")
print("")


def save_user(**user):  # ** is used to pass multiple keyword arguments to a function (or key value pairs, see output)
    print(user)         # so the (**user) is a dictionary
    # Below, using the key-name ["name"] we access its value ('John' in output)
    print(user["name"])


# Below we passed arbitrary Keyword Arguments in ()
save_user(id=1, name="John", age=22)
# Notice the syntax in the output (an obj called 'dictionary' i.e. {arguments})

print("")
print("")

### Scope ###
# "Refers to the region of the code where a variable is defined"

# message = "a"  # Global variable (outside the following function), the scope is this entire file.

# Below the scope of variable 'message' as well as the parameter 'name' ARE the 'greet' function.
# So they're local


# def say_hello(name):
# ..# message = "b" - scope of this variable would be inside the say_hello function

# say_hello("Mark") - This function call would cause a syntax error
# print(name) - here name is not defined
# print(message) - here Python would look at the message variable outside the function
#                   and print a

print("")
message = """ From Codecademy Discussion: """
print(message)
print("")


def introduction(first_name, last_name):
    print(f"{last_name}, {first_name} {last_name}")


introduction("John", "Doe")
print(introduction)

print("")


def introduction2(first_name, last_name):
    return f"{last_name}, {first_name} {last_name}"


message = introduction2("John", "Doe")
print(message)

###

print("")
message = """ Excercise: FizzBuzz Algorithm: """
print(message)
print("")

### Excercise: FizzBuzz Algorithm ###


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):   # The () are not necessary but code looks more readable
        return "FizzBuzz"  # Don't need to create a 'result' variable. We can return a string directly and eliminate a line of code!
    if input % 3 == 0:    # Don't need elif 'cause we return a value and if the previous if is false the code skips to the next step anyway
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input     # The indentetion for return allows us to skip else: because the previous ifs are all false


print(fizz_buzz(15))
