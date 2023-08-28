# Dictionaries

# Dictionary is an ordered collection of items. A dictionary has key-value pairs
# Values can be of any data category and can repeat
# Keys must be immutable and must be unique

# Creating a dictionary using curly braces {}

# empty dictionary
from turtle import clear

my_dict = {}
# dictionary with string keys
my_dictt = {'fruit': 'apple', 'vegetable': 'cucumber'}  # "fruit" is a key, and "apple" is his value

# Creating a dictionary using dict() function
dict_arguments = dict(name="George", age=22)  # key=value argument
# {"name": "George", "age": 22}

# You can write a dictionary on multiple lines
my_dicttt = {
    'fruit': 'apple',
    'vegetable': 'cucumber',  # Comma after every pair
    'diary': 'milk',
}

# What is a Key?

# While indexing is used with other container types to access values, dictionary uses keys
# Key can be used either inside square brackets or with the get() method
my_dictttt = {'name': 'Jack', 'age': 26}
print(my_dictttt['name'])  # Jack
print(my_dictttt.get('age'))  # 26
my_dictttt['address']  # KeyError
my_dictttt.get('address')  # None

# Change Values

# Dictionary is a mutable collection
# We can add new items or change the value of existing items using an assignment operator
# If the key is already present, value gets updated, else a new pair is added to the dictionary
my_dicttttt = {'name': 'Jack', 'age': 26}
my_dicttttt['age'] = 27  # update
print(my_dict['age'])  # 27

# Iterating Through Keys

# Using the keys() method to get all the keys from a dictionary
squares = {1: 1, 2: 4, 3: 9}
for key in squares.keys():
    print(key, end=" ")  # 1 2 3
# Changing the values by iterating through the keys
squares = {1: 1, 2: 4, 3: 9}
for key in squares.keys():
    squares[key] *= 2
# {1: 2, 2: 8, 3: 18}

# Iterating Through Values

# Using the values() method to get all the values
squares = {1: 1, 2: 4, 3: 9}
for value in squares.values():
    print(value, end=" ")  # 1 4 9

# We can also use the keys to get the values
squares = {1: 1, 2: 4, 3: 9}
for key in squares.keys():
    print(squares[key], end=" ")  # 1 4 9

# Iterating Using Items()

# Use the items() method to iterate through key-value pairs
# It returns tuple (key, value) pairs (tuples will be covered in the advanced course)
squares = {
    1: 1,
    2: 4,
    3: 9,
}
for (key, value) in squares.items():
    print(f"Key: {key}, Value: {value}")

# Checking for Existence

# Check for key existence by using the keys() method
my_dict = {'name': 'Peter', 'age': 22}
if 'name' in my_dict.keys():  # You can skip keys()
    print(my_dict['name'])  # Peter

# Check for value existence by using the values() method
my_dict = {'name': 'Peter', 'age': 22}
if 22 in my_dict.values():
    print("22 is a value in the dictionary")
# 22 is a value in the dictionary


# Dictionary Methods

# clear() - removes all the elements from a dictionary
my_dict = {1: 'apple', 2: 'banana'}
my_dict.clear()
print(my_dict)  # {}

# copy() - returns a copy of a dictionary
my_dict = {1: 'apple', 2: 'banana'}
copied_dict = my_dict.copy()
print(my_dict == copied_dict)  # True

# pop() - removes and returns an item from a dictionary having the given key
my_dict = {"fruit": "apple", "vegetable": "cucumber"}
apple = my_dict.pop("fruit")  # 'apple'
print(my_dict)  # {'vegetable': 'cucumber'}

# popitem() - removes an item that was last inserted and returns it as a tuple - (key, value)
my_dict = {"fruit": "apple", "vegetable": "cucumber"}
print(my_dict.popitem())  # ("vegetable": "cucumber")
print(my_dict)  # {"fruit": 'apple'}

# del keyword - removes an item with a specified key name
students = {"name": "George", "course": "Fundamentals"}
del students["course"]
print(students)  # {"name": "George"}

# del keyword can also delete the dictionary completely
students = {"name": "George", "course": "Fundamentals"}
del students
print(students)  # NameError


# What is Nested Dictionary?

# It is a collection of dictionaries into one single dictionary
# Nested dictionary's key have another dictionary as value
# Nested dictionaries are useful if you want to store a large amount of data in a structured way

# Creating nested dictionary
students = {1: {'name': 'Peter', 'age': 22},
	      2: {'name': 'Alex', 'age': 21}}

# Accessing an element
first_student_name = students[1]['name']
print(first_student_name) # Peter

# Adding an element
students[3] = {} # {3: {}}
students[3]['name'] = 'Amy' # {3: {'name': 'Amy'}}
students[3]['age'] = 25 # {3: {'name': 'Amy', 'age': 25}}

# Iterate through Nested Dictionary
# We use nested for-loop
shopping_list = {
    "foods": {"nuts": "almonds"},
    "drinks": {"soft": "lemonade", "wine": "merlot"}
}

for key, value in shopping_list.items(): # Using items() method
    for nested_key, nested_value in value.items():
        print(f'{nested_value} bought')
        shopping_list[key][nested_key] = 'bought'

# Dictionary Comprehensions

# Creating a dictionary using dictionary comprehension
data = [("Peter", 22), ("Amy", 18), ("George", 35)]
dictionary = {key:value for (key, value) in data}
# {'Peter': 22, 'Amy': 18, 'George': 35}

# Form a dictionary with cube values of numbers
nums = [1, 2, 3]
cubes = {num:num ** 3 for num in nums}
# {1: 1, 2: 8, 3: 27}

