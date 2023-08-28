stack = list()
n = int(input())
for i in range(n):
    query = input()
    if '1' in query:
        query = query.split(' ')
        stack.append(int(query[1]))
    elif '2' == query:
        if len(stack) > 0:
            stack.pop()
    elif '3' == query:
        print(max(stack))
    elif '4' == query:
        print(min(stack))

reversed_numbers = []
for n in range(len(stack)):
    reversed_numbers.append(str(stack.pop()))
print(', '.join(reversed_numbers))
