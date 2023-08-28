integers = input()
beggars = int(input())
list_with_integers = integers.split(", ")
filtered = []
for current_beggar in range(beggars):
    current_elements_received = 0
    for element in range(0, len(list_with_integers), beggars):
        current_elements_received += int(list_with_integers[element])
        list_with_integers.remove(list_with_integers[element])
    filtered.append(current_elements_received)
print(filtered)
