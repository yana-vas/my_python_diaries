# Tuple -> read-only collection -> immutable, but the objects inside are mutable
names = {"Test": 5}
b = (names,)
names.update({'Test2': 100})
print(b)

# METHODS
#           -> count()
a = (5, 2, 3, 5)
print(a.count(1))  # 2

#           -> index()
a = (10, 2, 3)
print(a[0])  # 10

# CREATING
t = (1, 2, 3)
t = 1, 2, 3
print(t)  # (1, 2, 3)
# -> visible_trees = (1, ) #creating a single element - we have to put comma after the element, so that the category of the variable can be tuple

# UNPACKING
data = (1, 2, 3)
x, y, z = data
# !!! if I assign not enough values, or assign more values than I need it will throw ValueError !!!
print('<->'.join([str(el) for el in data]))  # 1<->2<->3
print(*data)  # 1 2 3
print(*data, sep='<->')  # 1<->2<->3




# SET - it stores UNIQUE elements - collection which is unordered, unchangeable*, and unindexed.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# - елементите може да са на различни index всеки път когато ги достъпим.
# Може да си ги представим като кош(set) пълен с малки сфери, в които има някаква стойност,
# а тези сфери са всъщност нашите елменти.
# И ако трябва да наредим всички топки, ще започнем да ги вадим от този кош в разбъркан ред.
# т.е. в повечето случай когато се пробваме да ги подредим те ще са подредени по различен начин(разбъркан)
# If you try to add existing element in the set, it will just not add it
# Set items can be of any data category
# if you want to create an empty set you have to initialize it as set(), and not {}


# METHODS

# add()	-> Adds an element to the set
# remove() ->	Removes the specified element
# difference() ->	Returns a set containing the difference between two or more sets
# pop() ->	Removes an element from the set

# clear() ->	Removes all the elements from the set
# copy() ->	Returns a copy of the set
# difference_update() ->	Removes the items in this set that are also included in another, specified set
# discard() ->	Remove the specified item
# intersection() ->	Returns a set, that is the intersection of two or more sets
# intersection_update() ->	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint() ->	Returns whether two sets have a intersection or not
# issubset() ->	Returns whether another set contains this set or not
# issuperset() ->	Returns whether this set contains another set or not
# symmetric_difference() ->	Returns a set with the symmetric differences of two sets
# symmetric_difference_update() ->	inserts the symmetric differences from this set and another
# union() ->	Return a set containing the union of sets
# update() ->	Update the set with another set, or any other iterable


# Operators
# a = set([1, 2, 3, 4])
# b = set([3, 4, 5, 6])
# a | b # Union -> {1, 2, 3, 4, 5, 6}
# a & b # Intersection -> {3, 4}
# a < b # Subset -> False
# a > b # Superset -> False
# a - b # Difference -> {1, 2}
# a ^ b # Symmetric Difference -> {1, 2, 5, 6}


# a = set([1, 2, 3, 4])
# b = set([3, 4, 5, 6])
# a.union(b)			 # Equivalent to a | b
# a.intersection(b)         # Equivalent to a & b
# a.issubset(b)             # Equivalent to a <= b
# a.issuperset(b)           # Equivalent to a >= b
# a.difference(b)           # Equivalent to a - b
# a.symmetric_difference(b) # Equivalent to a ^ b

# Set Comprehension - use curly brackets {}
nums = [1, 2, 3, 4, 4, 5, 6, 2, 1]
unique = {num for num in nums}
# {1, 2, 3, 4, 5, 6}

