numbers_list = input().split(', ')
numbers_list = list(map(int, numbers_list))
even_index_numbers = [i for i in range(len(numbers_list)) if numbers_list[i] % 2 == 0]

# even_index_numbers = list()
#
# for i in range(len(numbers_list)):
#     if numbers_list[i] % 2 == 0:
#         even_index_numbers.append(i)
#
print(even_index_numbers)