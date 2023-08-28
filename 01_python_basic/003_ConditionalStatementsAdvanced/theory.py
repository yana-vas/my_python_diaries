#Само при изпълнение на първото условие се преминава към вложената проверка:
a = int(input())
b = int(input())
if a > b: # condition 1
    print('condition1 valid')
    if a == 3: # condition 2
        print('condition2 valid')
else:
    print('condition2 not valid')

# Оператори, които комбинират или изключват условия
# Връщат булев резултат (true или false)

# and - Вярност на двете условия - Проверява изпълнението на няколко условия едновременно
a = int(input())
if a > 5 and a < 10 and a % 2 == 0:
    pass
# if a > 5:
#     if a < 10:
#         if a % 2 == 0:


# or - Вярност на едното или на другото условие - Проверява дали е изпълнено поне едно измежду няколко условия
word = input()
if word == "Example" or word == "Demo":
    pass

# if word == 'Example':
# elif word == 'Demo':

# not - Отрицание на условие - Проверява дали не е изпълнено дадено условиe
number = int(input())
valid = number > 10 and number % 2 == 0
if not valid:
    print("Invalid")

#Чрез скоби ( ) можем да приоритизираме условия
a = 50
b = 200
c = 300
if (a >= 100 and b <= 200) or (c + b >= 300 and c <= 400):
    print("Yes") # Yes
if a >= 100 and (b <= 200 or c + b >= 300) and c <= 400:
    print("Yes") # No output