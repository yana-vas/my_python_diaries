
x = open("day_fifth_input_data.txt")


import re
from itertools import zip_longest

s = []

for line in x:
    if line == "\n":
        break
    s.append(line)

s.pop()
print(s)
st =[]

for line in s:
    print([line[i * 4 + 1] for i in range(len(line) // 4)])
    st.append([line[i * 4 + 1] for i in range(len(line) // 4)])


    # 1, 5, 9, 13, 17, 21, 25, 29, 33

print(st)

zipped = zip_longest(*st, fillvalue='')
zipped_list = list(zipped)

print(zipped_list)

s = [list("".join(c).strip()[::-1]) for c in zip_longest(*st, fillvalue='')]
print(f"{s=}")
print(len(s))

# First part:

for line in x:
    print(line)
    a, b, c = map(int, re.findall("\\d+", line))
    print(a ,b ,c)
    s[c - 1].extend(s[b - 1][-a:][::-1])
    s[b - 1] = s[b - 1][:-a]

print("".join([a[-1] for a in s]))

# Second part:

for line in x:
    a, b, c = map(int, re.findall("\\d+", line))
    s[c - 1].extend(s[b - 1][-a:])
    s[b - 1] = s[b - 1][:-a]

print("".join([a[-1] for a in s]))











# my_file = open("day_fifth_input_data.txt", 'r')
# seventh_day_input_data.txt = my_file.read()
# crane, commands = seventh_day_input_data.txt.split('\n\n')
# crane = crane.split('\n')
# length = int(crane[-1].strip()[-1])
# print(crane)
# # crane = [line.replace('   ', '[Ф]').split() for line in crane]
#
# curr_line = []
# my_dict = {}
# for counter in range(len(crane)-1):
#     curr_list = []
#     for i in range(len(crane)-1):
#         line = crane[i]
#         if counter in range(len(line)):
#             if line[counter] != '[Ф]':
#                 refactor_line = line[counter].replace('[Ф]', '')
#                 curr_list.append(refactor_line.replace('[Ф]', ''))
#     my_dict[counter + 1] = curr_list
# print(my_dict)
