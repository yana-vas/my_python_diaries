# Function == named piece of code
# Can take parameters and return result
def function_name(parameter: type): # Use snake-case; parameter - Function parameter; category - Type of the parameter
    # statement(s)

# Why Use Functions?
# More manageable programming
# Splits large problems into small pieces
# Better organization of the program
# Improves code readability
# Improves code understandability
# Avoiding repeating code
# Improves code maintainability
# Code reusability
# Using existing functions several times

# Function Without Parameters
# Executes the code between the brackets
# Does not return result
    def multiply_numbers():
        result = 5 * 5
        print(result)

    multiply_numbers()  # 25

# Declaring Function
def print_text(text):
  print(text)
# Using the def statement is the most common way to define a function in python
# Functions can have several parameters
# It is possible for function to not return a value

# Invoking a Function

# Functions are first declared, then invoked (many times)
def print_header(): # Function Declaration
  print("----------")

# Functions can be invoked (called) by their name:
def main(): # Function Invocation
  print_header()

# A function can be invoked from:
# Other functions
def print_header():
    pass
  # print_header_top()
  # print_header_bottom()

# Itself (recursion)
def crash():
   crash()

# Functions can return a value that you can use directly:
def give_me_five():
    return 5
print(give_me_five())  # Print the returned value
#Out: 5

# or save the value for later use:
num = give_me_five()
print(num) #Print the saved returned value
#Out: 5


# If return is encountered in the function the function will be exited immediately
def give_me_another_five():
	return 5
	print('This statement will not be printed.')
print(give_me_another_five()) #Out: 5

# Parameter is variable defined in function definition, while argument is actual value passed to the function
def solve(grade): # grade - > parameter
    pass
solve(6) # 6 -> argument

# Default Arguments
# Function arguments can have default values
# If the function is called without the argument, the argument gets its default value
def person(first_name = 'George', last_name ='Brown'):
    print(first_name, last_name)
person() #'George Brown'

# Keyword (Named) Arguments
# Functions can be called using keyword arguments
# When we use keyword/named arguments, it's the name that matters, not the position
def area(width, height):
    return width * height
print(area(height = 2, width = 1))


# Summary
# Break large programs into simple functions that solve small sub-problems
# Consist of declaration and body
# Are invoked by their name
# Can accept parameters



