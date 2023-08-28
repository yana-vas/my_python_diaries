name = input() #Команда за четене от конзолата
print("My name is " + name) #Връща ни "My name is " + текстът, въведен от потребител

data = input() # същото като scanner в Java

num = int(data) #Четене на цяло число от конзолата; num = int(data) == num = int(input())

num = float(data) #Четене на дробно число от конзолата; == num = float(input())

print("Hello, ", end="") #Курсорът остава на същия ред
print(name) #name = "Yana" -> output: Hello, Yana

print("Hello, ")
print(name) #name = "Yana' -> output: Hello,
#                                     Yana

name = input()
print('Hello, ' + name) #name = "Yana" -> output: Hello, Yana

#Съединяване на текст и число (оператор +):
first_name= 'Maria'
last_name= 'Ivanova'
age = 19
str = first_name + ' ' + last_name + ' @ ' + str(age)
print(str) # Maria Ivanova @ 19
#Резултатът е долепяне/конкатенация

a = 1.5
b = 2.5
sum = 'The sum is: ' + str(a) + str(b) #Превръщане на числена стойност в текст
print(sum) # The sum is 1.52.5

#Събиране на числа (оператор +):
#Изваждане на числа (оператор -):
#Умножение на числа (оператор *):
#Деление на числа (оператор / и //):
a = 25
f = a / 4 # 6.25
i = a // 4 # 6 - целочислено деление (//)
error = a / 0 # Грешка: деление на 0

#Модул/остатък от целочислено деление на числа (оператор %):
a = 7
b = 2
product = a % b #1 -> 7/2 = 3 => 1 remainder -> 3+3 =! 7

#Можем да форматираме изхода чрез интерполация, която се означава със символа 'f':
first_name = input()
last_name = input()
age = int(input())
town = input()
print(f"You are {first_name} {last_name}, a {age}-years old person from {town}.") #В къдравите скоби поставяме името на променливата

#използване на вече готови програми
#import Името на библиотеката “ За целта трябва да ги "заредим"

# import math
# Зарежда библиотеката с име math
#
# import sys
# Зарежда библиотеката с име sys
#
# import math, sys
# Зарежда всички изредени библиотеки



