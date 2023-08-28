number_of_groups = int(input())

p_musala = 0
p_monblan = 0
p_kilimandgaro = 0
p_K2 = 0
p_Everest = 0
for i in range(number_of_groups):
    number_of_people = int(input())
    if number_of_people <= 5:
        p_musala += number_of_people
    elif number_of_people <= 12:
        p_monblan += number_of_people
    elif number_of_people <= 25:
        p_kilimandgaro += number_of_people
    elif number_of_people <= 40:
        p_K2 += number_of_people
    else:
        p_Everest += number_of_people
everyone = p_musala + p_monblan + p_kilimandgaro + p_K2 + p_Everest

print(f"{p_musala / everyone * 100:.2f}%")
print(f"{p_monblan / everyone * 100:.2f}%")
print(f"{p_kilimandgaro / everyone * 100:.2f}%")
print(f"{p_K2 / everyone * 100:.2f}%")
print(f"{p_Everest / everyone * 100:.2f}%")
