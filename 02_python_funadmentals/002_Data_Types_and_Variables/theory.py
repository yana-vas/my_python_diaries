#In Python, escape sequences are indicated by a backslash ( \ ).
s = 'Jordan\'s car'
print(s)

#конкатенация
first_name = input()
last_name = input()
delimeter = input()
print(f"{first_name}{delimeter}{last_name}")

#The join in Python takes all the elements of an iterable and joins them into a single string. It will return the joined string.
# You have to specify a string separator that will be used to separate the concatenated string.
sentence = ['this', 'is', 'a', 'sentence']
'-'.join(sentence)
#'this-is-a-sentence'


