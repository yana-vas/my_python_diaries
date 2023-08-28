input_data = open("comments", 'r').read()
input_data = input_data.split('\n')
input_data = ' '.join(input_data)
print(input_data)