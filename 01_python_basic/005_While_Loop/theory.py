#while ...(условие)...
    # code (Код за изпълнение (повторение))
# докато условието е вярно минавай през цикъла, изпълнявай кода
# a = 5
#
# while a <= 10:
#     print("a = " + str(a))
#     a += 1
#Условие за прекратяване на повторението
# докато "а" е по-малко или равно на 10 принтирай "а" и след всяка итерация добавяй единица към стойността "а"

#---------------------------------------------------------------------------------------------------------------------------------


# line = input
#
# while line != "Stop":
#     print("Loop")
#     line = input()
# Условие за прекратяване на повторението
#докато line(текстът който си написал на конзолата) не е равно на "Stop" принтирай "Loop" и напиши нова стойност на line


#Безкраен цикъл – повтаряне на блок от код безкраен брой пъти:
while True: # Условието е винаги вярно
    print("Infinite loop")

#Оператор break – прекъсва цикъла
# Не може да съществува самостоятелно извън цикъл
while True:
    print("Loop")
    if...: #Условие за прекъсване на цикъла
        break
# example
a = 5

while True:
    if a > 10:
        break
    print("a = " + str(a))
    a += 1
# example 2

while True:
    line = input()
    if line == "Stop":
        break
    print("Loop")
    