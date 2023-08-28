first_sequence = {int(x) for x in input().split()}
second_sequence = {int(x) for x in input().split()}
n = int(input())

for _ in range(n):
    command = input().split()
    new_sequence = {int(x) for x in command[2:]}
    if command[0] == 'Add' and command[1] == 'First':
        first_sequence = first_sequence.union(new_sequence)
    elif command[0] == 'Add' and command[1] == 'Second':
        second_sequence = second_sequence.union(new_sequence)
    elif command[0] == 'Remove' and command[1] == 'First':
        first_sequence.difference_update(new_sequence)
    elif command[0] == 'Remove' and command[1] == 'Second':
        second_sequence.difference_update(new_sequence)
    elif command[0] == 'Check' and command[1] == 'Subset':
        print(first_sequence.issuperset(second_sequence))

print(f"{', '.join(list(map(lambda x: str(x), sorted(first_sequence))))}")
print(f"{', '.join(list(map(lambda x: str(x), sorted(second_sequence))))}")