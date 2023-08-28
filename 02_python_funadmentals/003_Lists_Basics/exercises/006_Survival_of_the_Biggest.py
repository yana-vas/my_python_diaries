import sys

list_numbers = input().split(" ")
n = int(input())
for i in range(n):
    min_number = sys.maxsize
    for element in list_numbers:
        if int(element) < min_number:
            min_number = int(element)
    list_numbers.remove(str(min_number))
print(", ".join(list_numbers))
