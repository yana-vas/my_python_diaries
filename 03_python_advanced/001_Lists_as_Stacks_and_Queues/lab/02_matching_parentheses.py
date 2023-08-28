expression = input()

index_stack = []
for i in range(len(expression)):
    if expression[i] == '(':
        index_stack.append(i)
    elif expression[i] == ')':
        start_index = index_stack.pop()
        print(expression[start_index:i+1])