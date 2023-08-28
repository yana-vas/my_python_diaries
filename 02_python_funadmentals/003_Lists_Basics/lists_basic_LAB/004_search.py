n = int(input())
word = input()

my_list = []
filtered = []
for i in range(n):
    current_string = input()
    my_list.append(current_string)
    if word in current_string:
        filtered.append(current_string)
print(my_list)
print(filtered)

##########################################

# n = int(input())
# word = input()
#
# my_list = []
# for i in range(n):
#     my_list.append(input())
#
# filtered = []
# for current_string in my_list:
#     if word in current_string:
#         filtered.append(current_string)
# print(my_list)
# print(filtered)