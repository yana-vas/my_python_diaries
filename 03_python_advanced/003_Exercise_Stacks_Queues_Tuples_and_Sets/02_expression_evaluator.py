import math
from collections import deque

expression = input().split()
numbers = deque()
operator = ''
result = 0
for char in expression:
    if char.isdigit() or len(char) > 1:
        numbers.append(int(char))
    else:
        result = int(numbers.popleft())
        operator = char

        while numbers:
            if char == '-':
                result -= numbers.popleft()
            elif char == '+':
                result += numbers.popleft()
            elif char == '*':
                result *= numbers.popleft()
            elif char == '/':
                result /= numbers.popleft()
                result = math.floor(result)
        numbers.append(result)
print(result)