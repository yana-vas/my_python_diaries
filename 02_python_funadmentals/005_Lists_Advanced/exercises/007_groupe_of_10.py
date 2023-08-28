import sys

numbers = list(map(int, input().split(', ')))
max_num = -sys.maxsize
for current_num in numbers:
    if current_num > max_num:
        max_num = current_num
if len((str(max_num))) == 1:
    max_num_tents = 10
else:
    if int(str(max_num)[1]) == 0:
        max_num_tents = max_num
    else:
        max_num_tents = (int((str(max_num))[0]) + 1) * 10

for tents in range(10, max_num_tents+1, 10):
    current_tents = list(filter(lambda num: num <= tents, numbers))
    numbers = [num for num in numbers if num not in current_tents]
    print(f"Group of {tents}'s: {current_tents}")
