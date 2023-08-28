# списъкът се използва за трансфериране на информацията от едно място на друго
# списъкът се използва да държим повече данни в една променлива
#A list is a collection which is index supported and changeable (mutable)
# It allows duplicate members and in Python lists are written with square brackets
# Lists are very useful for storing multiple elements
# it can store elements with different data types

list_example = ["apple", "banana", "cherry"]
#creating a list
# Lists in Python can be created by just placing the sequence inside the square brackets
my_list = [1, 2, 3]
#creating empty list
empty_list = list() #using the list function
emptyList = [] # creating a list with 0 elements in it
#a list may contain duplicate values
my_list = [1, 2, 3, 2, 3, 3]

# You can use the split function to split a string and create a list
some_text = "a b c d"
my_list = some_text.split(" ") #разделяме текстът с " " (space) на отделни елементи - ще раздели теекста тм където б=види спейс. Тоест започва първата буква- 'а' оставая. Продължава със следващият символ - той е ' ', което означава че 'а' ще стане отделен елемент в my_list
print(my_list)
# ['a', 'b', 'c', 'd']

some_text = "a, b, c, d"
my_list = some_text.split(", ") #разделяме текстът с ", " (space) на отделни елементи
print(my_list)
# ['a', 'b', 'c', 'd']

# You can create a string from a list using join function
my_list = ["a", "b", "c"]
print("-".join(my_list)) # след всеки един елемент ще долепи "-" и ще го превърне в string
# a-b-c


# in Python you can only join list of strings
print(" ".join([1, 2, 3])) # this will NOT WORK

# use square brackets to get an element by an index -> the name of the list + [ + index + ]
# Indices describe the position of an element
# we always start counting from 0
list_of_numbers = [1, 5, 7]
print(list_of_numbers[0]) # 1
print(list_of_numbers[1]) # 5
print(list_of_numbers[2]) # 7

# You can use the negative sign to access an element
# The negative sign will start counting from the end of the list
my_pets = ["cat", "dog", "parrot"]
print(my_pets[-1]) # parrot
print(my_pets[-2]) # dog
print(my_pets[-3]) # cat

#Adding to a List

#use the append function to add a new element
empty_list = []
empty_list.append(2)
empty_list.append(3)
print(empty_list)
# [2, 3]

my_list = ['milk', 'bread', 'water']
my_list.insert(1, 'flour')
print(my_list)
# ['milk', 'flour', 'bread', 'water']

# Removing from a List

# use the remove function to remove a particular element
list_of_numbers = [1, 2, 3, 4, 5]
list_of_numbers.remove(3)
list_of_numbers.remove(1)
print(list_of_numbers)
# [2, 4, 5]


# Looping through Lists

#iterating over the elements
my_list = ["dog", "cat", "fish"]
for element in my_list:
    print(element, end=" ") # dog cat fish

#using generated list with range
for index in range(len(my_list)):
    print(my_list[index], end=" ")

# Using while loop

#iterating until we reach the end of the list
my_list = ["dog", "cat", "fish"]
i = 0
while i < (len(my_list)) :
    print(my_list[i], end=" ")
    i += 1

#iterating until there are no more elements in the list
while my_list:
    print(my_list[0], end=" ")
    current_element = my_list[0]


# можем да правим логически изрази, с които да проверяваме дали даден елемент е в списъкът

# use the keyword "in" to check if an element is in a list (usually the "in" and "not in" keyword is used in if-else statements)
my_list = [1, 2, 3, 4,]
if 3 in my_list:
    print("The number 3 is in the list :)")

# use the keyword "not in" to check if an element is NOT in a list
if 5 not in my_list:
    print("The number 5 is not in the list :(")

# delete repeated elements in a list
while 3 in my_list:
    my_list.remove(3)

# Slicing
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array