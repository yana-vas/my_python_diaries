# Comprehensions provide us with a short way to construct new sequences
# They allow sequences to be built from other sequences
# They require less memory
# They have shorter syntax and better performance

# A list comprehension consists of the following parts:
# An input sequence
# A variable representing members of the input sequence
# An optional predicate expression
# An output expression producing elements in the output list

# Creating a list using the range function
x = [num for num in range(5)]  # num -> output expression; num -> variable
# [0, 1, 2, 3, 4]

# Creating a list with only zeros using the range function
x = [0 for num in range(5)]
# [0, 0, 0, 0, 0]

# Getting the square values of numbers in a list
nums = [1, 2, 3, 4]
squares = [x ** 2 for x in nums]  # for every element in nums add in squares the element on power of 2
# [1, 4, 9, 16]

# Using if statement in a list comprehension
nums = [1, 2, 3, 4, 5, 6]
evens = [num for num in nums if
         num % 2 == 0]  # for every element in nums if num % 2 == 0 (if the element(num) is even) add the element in evens
# [2, 4, 6]

# Using if-else statement in a list comprehension
nums = [1, 2, 3, 4, 5, 6]
filtered = [True if element % 2 == 0 else False for element in
            nums]  # for every element in nums add True if the element is even otherwise add False
# [False, True, False, True, False, True]

# Adding Elements
# Using the append() method - Add single element at the end
my_list = [1, 2, 3]
my_list.append(4)  # [1, 2, 3, 4]

# Using the extend() method - Add multiple elements at the end
my_list = [1, 2, 3]
my_list.extend([4, 5])  # [1, 2, 3, 4, 5]

# Using the insert() method - Add single element at a specific index
my_list = [1, 2, 3]
my_list.insert(1, 4)  # [1, 4, 2, 3]

# Removing Elements

# Using the clear() method - Removes all elements
my_list = [1, 2, 3]
my_list.clear()  # []

# Using the pop() method - Removes element by index and returns it
my_list = [1, 2, 3]
number = my_list.pop(0)  # [2, 3]; number -> 1

# Using the remove() method - Removes by value (first occurrence)
my_list = [1, 2, 3]
my_list.remove(1)  # [2, 3]

# More Useful Methods

# Using the count() method - Finds all occurrences in a list
my_list = [1, 2, 3, 2, 2]
my_list.count(2)  # 3

# Using the index() method - Finds the index of the first occurrence
my_list = [1, 2, 3, 2, 2]
last = my_list.index(2)  # 1

# Using the reverse() method - Reverses the elements
my_list = [1, 2, 3]
my_list.reverse()  # [3, 2, 1]

# sorted()  Function
# Sorts the elements of a list in ascending order
numbers_list = [6, 2, 1, 4, 3, 5]
sorted_numbers = sorted(numbers_list)
# [1, 2, 3, 4, 5, 6]

# Sorts the elements of a list in descending order
numbers_list = [6, 2, 1, 4, 3, 5]
sortd_numbers = sorted(numbers_list, key=lambda x: -x)
# [6, 5, 4, 3, 2, 1]

# map() Function
# map() - имаме списък, който е готв и вече на този списък може да направим нещо в/у него
# Use it to convert list of strings to list of integers - Returns int(x) for each element x in the list
strings_list = ["1", "2", "3", "4"]
numbers_list = list(map(int, strings_list))  # [1, 2, 3, 4]

# It applies function to every item of an iterable
numbers_list = [1, 2, 3, 4]
doubled_list = list(map(lambda x: x * 2, numbers_list))  # for each element x from numbers_list multiply it by 2


# [2, 4, 6, 8]
# map() function returns a map object(which is an iterator)
# of the results after applying the given function to each item of a given iterable (list, tuple etc.)
# Syntax :
# map(fun, iter)
# Parameters :
# fun : It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.

# It returns an iterator object, so you need to convert it into a list

# lambda() - анонимна функия, която приема един параметър и връща някаква стойност
# Python code to illustrate cube of a number
# showing difference between def() and lambda().
def cube(y):
    return y * y * y


lambda_cube = lambda y: y * y * y

# using the normally
# defined function
print(cube(5))

# using the lambda function
print(lambda_cube(5))

# Without using Lambda: Here, both of them return the cube of a given number.
# But, while using def, we needed to define a function with a name cube and
# needed to pass a value to it. After execution, we also needed to return
# the result from where the function was called using the return keyword.

# Using Lambda: Lambda definition does not include a “return” statement,
# it always contains an expression that is returned. We can also put a lambda
# definition anywhere a function is expected, and we don’visible_trees have to assign it
# to a variable at all. This is the simplicity of lambda functions.


# filter() function - Use it to filter elements that fulfill a given condition
# проверяваме дали този елемент отговаря на дадена функционалност
# когато използваме filter(), тази анонимна функция ни филтрира само числата, които са четни
# подобно на list comprehension - създаваме нов лист  и добавяме елементите от друг list, които отговарят на дадено условие
numbers_list = [1, 2, 3, 4, 5, 6]
even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers_list))  # правим анонимна функция, която връща сравнение - връща True или False
# [2, 4, 6]
# The lambda should return either True or False
# It returns an iterator object, so you need to convert it into a list

# map()  and filter() returns an iterator object, so you need to convert it into a list

names = input().split(", ")

sorted_names = sorted(names)  # сортиране по азбучен ред
sorted_names = sorted(sorted_names, key=lambda name: -len(name))  # сортира ги по дължината на името отзад напред -
# sort the names in ascending order (alphabetically)
# и двете са еднакви
whole_sorted_names = sorted(names, key=lambda name: (
    -len(name), name))  # първо сортира по дължината на думата по азбучен ред и полсе проверява името

# Swapping List Elements
# You can use the following syntax to swap two or more list elements
nums = [1, 2, 3]
nums[0], nums[1], nums[2] = nums[2], nums[0], nums[1]  # [3, 1, 2]
# The first element on the left swaps with the first on the right etc.

# Concatenating Lists
# You can use the "+" operator to join two lists
nums_list_1 = [1, 2, 3]
nums_list_2 = [4, 5, 6]
print(nums_list_1 + nums_list_2)  # [1, 2, 3, 4, 5, 6]
# Always the second list is added at the end of the first

# The Set Function
# You can use the set() function to extract only the unique elements from a list
numbers = [1, 2, 2, 3, 4, 1, 4, 5]
unique_numbers = list(set(numbers))  # [1, 2, 3, 4, 5]
# The set() function returns a set with the unique values
# You will learn more about sets in the advanced python module

# Useful methods

print(list(range(11)))  # prints a list with the numbers from 0 to 10
print([x for x in range(11)])  # prints a list with the numbers from 0 to 10

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del my_list[1:5] # removes all elements form index 1 to index 5 -> output: [1, 6, 7, 8, 9, 10]

# using command prompt - python try help(list) - you will be given the documentation of lists and all methods like: append(), insert() and others