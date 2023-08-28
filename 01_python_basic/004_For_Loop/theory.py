# Циклите в програмирането ни позволяват да повтаряме едни и същи действия определен брой пъти

for i in range(1, 13):
    print(i)
# i = 1 ако i <= 12 -> print(i) else -> end loop

# for - ключова дума за конструкцията
# 1 - начална стойност
# 13 - крайна стойност +1
# print(i) - тяло на цикъла: блок от кода за повторение

#Можем да повтаряме действия до определен момент чрез for-цикли

# For-цикъл със стъпка

# Можем да използваме стъпка ако искаме да променяме стойността на i със стойност различна от 1
for i in range(2, 11, 2): # Задаване на стъпка 2
    print(i)
# Стъпката може да бъде негативна
for i in range(11, 0, -2): # Задаване на стъпка -2
    print(i, end=" ")

# Упражнение
# Числата от 1 до N през 3 – решение
n = int(input())
for i in range(1, n + 1, 3): # Задаване на стъпка 3
    print(i)
#1. read n; 2. n = 1; 3. i <= n; 3.1 true -> print i; false -> xit the loop
#                                             i += 3




# При определяне на диапазон използваме само цели числа.
# Използваме for цикъл, само когато знаем колко точно итерации трябва да направи --> range().
# Винаги имаме крайна стойност на итерациите.
# Променлива, която променя стойността си при всяка итерация.
# Работи само с цели числа.

# for number in range(x, y, z):     # X е старт(с кое число искаш да започнеш)
#     pass                          # Y е край(крайна стойност(цикълът ще се изпълнява докато X < Y или X <= Y+1))
                                    # Z e стъпка(какво ще се промени на следващата итерация(колко ще се добавящ след всяка итерация)АКО НЕ НАПИШЕМ СТЪПКАТА, ТЯ АВТОМАТИЧНО ЩЕ Е РАВНА НА 1)
                                    # (start, end, step)

                                    # for number in range (10) - това е само крайната стойност
                                    # for number in range (0, 10) - това е ако решим да изписваме 0, но може и горния пример


# for number in range(x, y):     # За променливата (number) в диапазона
# for number in range(y):        # x който го няма в този приммер, започва от 0


# for number in range(1, 10):   # if 1 <= number < 10 това цялото нещо изпълнява същата функция
#     print(number)

# for number in range(10):        # Изписвайки само крайната стойност, стартовата стойност е 0
#     print (number)

# for number in range(10):        # Изписва 10 пъти Hello
#     print("Hello")

# for number in range(1, 20, 1):    #Ще изпише нормално от 1 до 19
#     print(number)

# for number in range(2, 20, 2):      #Ще принтира само четните числа, стъпка 2
#     print(number)

#for number in range (20, 1, 2):     # Няма да се изпълни този цикъл.
#for number in range (20, 1, -2):     # с тази стъпка -2, ще започне от 20 и ще изважда -2 към крайна стойност 1.
#    print(number)

# for number in range (1, 10 +1)       # Крайната стойност ще е 10
#     print(number)

# for number in range (1,10 +1):
#     print(number)
#     number += 100
#     print(number)

# for number in range (1,10 +1):        # 10 пъти ще повтаря операцията в цикъла.
#     number2 = 10
#     print(number2)
#     number2 += 100
#     print(number2)

# for number in range (1, 200):
#     if number % 2 == 0:
#         print(number)
#         continue           # Използва се само в тялото на цикъла. Означава не се интересувай какво има надолу а продължи пак от горе.
#         break              # Обратното на continue. Спира и нито надолу, нито нагоре. Излиза от цикъла.
#     print("Number is odd")

# text = input()
# print(text)

# text = input()           #отпечатва въвдените букви на текста
# for letter in text:
#     print(letter)

# text = input()           #Работа с индекс. Първата буква на текста започва от 0.
# print(text[0])
# print(text[4])
# print(text[5])

# text = input()
# for index, character in enumerate(text):                 #Извърта цикъла едновремено индекса и символа
#     print(f'Index->{index}, character ->{character}')


# Можем да вземем дължината на текст
text = "SoftUni"
length = len(text)     # 7
# Можем да вземем символ от текст по индекс
text = "SoftUni"
letter = text[4]  # U

# It looks like ord() works for any Unicode codepoint. And chr() would perform the inverse.
current_input = 'I'
print(ord(current_input))
# output -> 73
current_input = 73
print(chr(current_input))
# output -> I