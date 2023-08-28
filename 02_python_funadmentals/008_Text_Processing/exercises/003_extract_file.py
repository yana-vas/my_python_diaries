input_data = input().split('\\')
my_file = input_data[-1].split('.')
file_name = my_file[0]
file_extension = my_file[1]
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")