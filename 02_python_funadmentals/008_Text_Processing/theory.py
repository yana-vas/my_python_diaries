# Text Processing

# String - sequence of Unicode  characters

# A string is a sequence of characters
# A character is simply a symbol
# Computers do not deal with characters, they deal with numbers
# A character is stored and manipulated as a combination of 0's and 1's

# String Literals - are surrounded by either single quotation marks, or double quotation marks
# You can display a string literal with the print() function

# Assign String to a Value - variable name followed by an equal sign and the string
a = 'Hello' # name -> a, equal sign, string -> 'Hello'

# Assign a multiline string to a variable by using three quotes
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit, sed do eiusmod tempor 
incididuntut labore et dolore magna aliqua."""

# Methods

str() # the function converts the specified value into a string
x = str(3.5) # x = "3.5"

# The split() method splits a string into a list
txt = "hello, my name is Peter, I am 26 years old"
lst = txt.split(", ") # # ["hello", "my name is Peter", "I am 26 years old"]

# Concatenation

# Use the "+" operator to merge strings
str1 = 'Hello'
str2 = "World"
str3 = str1 + str2 # "HelloWorld"

# The "*" operator repeats the string
str1 = 'red'
print(str1*3) # "redredred"

# String Formatting

# "f-String" is the most used way for string formatting
x = 'apples'
y = 'bananas'
z = f'In the basket are {x} and {y}' # "In the basket are apples and bananas"

# Formatting with the "%" operator
x = 'apples'
y = 'bananas'
z = 'In the basket are %s and %s' % (x, y)

# Formatting with the "{}" operators
x = 'apples'
y = 'lemons'
z = "In the basket are {} and {}".format(x, y)

# Substring - Slicing
# It is equivalent to the slice() method

# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array

list_example = ["python","ruby","java","javascript","c#","css","html"]
print(list_example[0:3]) #will print the programming language under python and javascript -
# ['python', 'ruby', 'java']
print(list_example[3:]) # will print the programming language from javascript to the last element(language) -
# ['javascript', 'c#', 'css', 'html']
print(list_example[:3]) # all languages under python to javascript -
# ['python', 'ruby', 'java']
print(list_example[:]) # all languages -
# ['python', 'ruby', 'java', 'javascript', 'c#', 'css', 'html']


# String Methods

# Check if a character is a digit: isdigit()
'1'.isdigit() # True
'p'.isdigit() # False

# Check if a character is upper/lower case: isupper() and islower()
'P'.isupper() # True
'P'.islower() # False
'u'.islower() # True

# Convert to upper/lower case: upper() and lower()
"hello".upper() # "HELLO"
"HeLLo".lower() # "hello"

# Remove white spaces in start/end or both: strip(), rstrip() -> right strip, lstrip() -> left strip
" hello ".lstrip() # "hello "
" hello ".rstrip() # " hello"
" hello ".strip() # "hello"

# You can use the replace() method to replace all occurrences of a specified phrase with another specified phrase
txt = "I like bananas"
print(txt.replace("bananas", "apples")) # "I like apples"

# If you only want to replace a certain number of phrases, add count
txt = "I like bananas bananas bananas"
x = txt.replace("bananas", "apples", 2) # "I like apples apples bananas"

# reverse a string
string = "racecar"
print(string[::-1])

