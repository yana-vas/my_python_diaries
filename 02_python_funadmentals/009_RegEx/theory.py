# positive look behind - (?<=\s)
# намери един интервал и после почни да търсиш по regex pattern

# RegEx - a sequence of characters that define a search pattern

# Special Sequences
# \d - contains digits (numbers from 0-9)
# \D - DOES NOT contain digits
# \b - the specified characters are at the beginning or at the end of a word
# \s - contains a white space character
# \S - DOES NOT contain a white space character
# \w - contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
# \w- DOES NOT contain any word characters

# Metacharacters
# \ - Signals a special sequence (can also be used to escape special characters)
# . - Any character (except newline character)
# + - One or more occurrences
# * - Zero or more occurrences
# | - Either or
# () - Capture and group
# {} - Exactly the specified number of occurrences
# ^ - Starts with
# $ - Ends with

# Sets
# [arn] - Returns a match where one of the specified characters (a, r, or n) are present
# [a-n] - Returns a match for any lower-case character, alphabetically betweena and n
# [^arn] - Returns a match for any character EXCEPT a, r, and n
# [0123] - Returns a match where any of the specified digits (0, 1, 2, or 3) are present
# [0-9] - Returns a match for any digit between 0 and 9
# [0-5][0-9] - Returns a match for any digit between 0 and 9
# [a-zA-Z] - Returns a match for any character alphabetically between a and z,lower case OR upper case


# RegEx Module
# Python has a built-in package called re
# It can be used to work with Regular Expressions
# Import the re module
import re
# Use it to search in text
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)


# findall() method - returns a list containing all matches
import re
str = 'The rain in Spain'
x = re.findall('ai', str)
print(x) # ['ai', 'ai]
# The list contains the matches in the order they are found
# If no matches are found, an empty list is returned

# search() method - searches the string for a match, and returns a Match object if there is a match
# If there is more than one match, only the first occurrence of the match will be returned
import re
str = 'The rain in Spain'
x = re.search('\s', str)
print(x.start())
# If no matches are found, the value None is returned

# split() method - function returns a list where the string has been split at each match
import re
str = 'The rain in Spain'
x = re.split('\s', str)
print(x)
# ['The', 'rain', 'in', 'Spain']
