start_number = int(input())
end_number = int(input())
magic_number = int(input())
combination_counter = 0
found_equation = 0
for i in range(start_number, end_number +1):
    if found_equation != 0:
        break
    for j in range(start_number, end_number +1):
        combination_counter += 1
        if (i + j) == magic_number:
            found_equation += 1
            print(f"Combination N:{combination_counter} ({i} + {j} = {magic_number})")
if found_equation == 0:
    print(f"{combination_counter} combinations - neither equals {magic_number}")

