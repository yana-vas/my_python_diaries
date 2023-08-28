# num = 0
# for number in range(10, 10+1):
#     num += 1
#     print(f"Hello {num}")

# for number in range(1, 10 + 1):
#     print(number)
     # number += 100
     # print(number)

# for number in range(1, 200):
#     if number % 2 == 0:
#         print(number)
#         continue
#         print("Let's do it!")
#
# print("How this works?")

# text = input()
# for letter in text:
#     print(letter)

# text = input()
# print(text[0])
# print(text[1])
# print(text[2])

# text = input()
# for index, character in enumerate(text):
#     print(f'Index->{index}, character ->{character}')
# OUTPUT:
# yana
# Index->0, character ->y
# Index->1, character ->a
# Index->2, character ->n
# Index->3, character ->a
import sys
n = int(input())

smallest = sys.maxsize
biggest = -sys.maxsize
for i in range(n):
    num = int(input())
    if num > biggest:
        biggest = num
    elif num < smallest:
        smallest = num

print(f"Max number: {biggest}")
print(f"Min number: {smallest}")
