# Conditions
import math

a = 5
b = 10
print(a < b) #true
print(a > 0) #true
print(a > 100) #false
print(a < a) #false
print(a <= 5) #true
print(b == 2 * a) #true

a = 'Examplе'
b = a
print(a == b) #True

a = input()
b = input()
print(a == b) #True

#Boolean
a = 5
is_positive = a > 0
print(is_positive) # True

a = -5
is_positive = a > 0
print(is_positive) # False


a = 5
is_positive = a > 0
print(is_positive) # True

a = -5
is_positive = a > 0
print(is_positive) # False


#Табулациите въвеждат блок от код (група команди)
# Изпълнява се редът, който отговаря на условието
color = 'red'
if color == 'red':
    print('Red')
else:
    print('Yellow')
    print('bye')  #Red

#Без табулации ще се изпълнява и последният ред
color = 'red'
if color == 'red':
    print('Red')
else:
    print('Yellow')
print('bye')   #Red
               #bye

# В програмирането можем да закръгляме дробни числа!!!!!!!

#Закръгляне до следващо (по-голямо) цяло число:
up = math.ceil(23.45) # 24
# Закръгляне до предишно (по-малко) цяло число:
down = math.floor(45.67) # 45

#Намиране на абсолютна стойност
example1 = abs(-50) # 50
example2 = abs(50) # 50


#Закръгляне до 2 знака след десетичния знак:
#банкерско закръгляне - ако числото след 2-рият знак е по-голямо от 5 тогав добавяме единица към последното цифра на числото, ако числото е 45.6785 и ние искаме да закръглим до 2 знак след десетичния знак, тогава резултаът на закръгленото число ще е: 45.68
rounded = round(45.67852, 2) # 45.68
#Форматиране до 2 знака след десетичния знак:
print(f"{123.456:.2f}") # 123.46

#серия от проверки
if ...:
    pass
    # code
elif ...:
    pass
    #code
elif ...:
    pass
    # code
else:
    pass
    # code

#При истинност на едно условие, не се продължава към проверяване на следващите условия

a = 7
if a > 4:
    print('Bigger than 4')
elif a > 5:
    print('Bigger than 5')
else:
    print('Equal to 7') # Bigger than 4

    #Променливата salary ще съществува само акое инициализирана някъде в програмата
current_day = "Monday"
if current_day == "Monday":
    salary = 1000
print(salary) # 1000
    #Променливата salary няма да съществува, ако не бъде инициализирана някъде в програмата
current_day = "Tuesday"
if current_day == "Monday":
    salary = 1000
print(salary) # Error