from collections import deque

import math

def solve(monkey):
    for item in monkeys[monkey]['items']:
        worry_level = item
        if operation[0] == '*':
            if operation[1] == 'old':
                worry_level *= worry_level
            else:
                worry_level *= int(operation[1])
        elif operation[0] == '+':
            if operation[1] == 'old':
                worry_level += worry_level
            else:
                worry_level += int(operation[1])
        # worry_level = math.floor(worry_level / 3)
        if worry_level % monkeys[monkey]['test']['divisible by'] == 0:
            name = monkeys[monkey]['test']['true']
            monkeys[name]['items'].append(worry_level)
        else:
            name = monkeys[monkey]['test']['false']
            monkeys[name]['items'].append(worry_level)
        monkeys[monkey]['inspected items'] += 1
        monkeys[monkey]['items'] = []


input_data = open('input_data.txt').read().split('\n\n')
monkeys = {}

for line in input_data:
    line = line.split('\n ')
    items = [int(i) for i in line[1].split(': ')[-1].split(', ')]
    name = line[0][:-1].lower()
    monkeys[name] = {}
    monkeys[name]['items'] = items
    monkeys[name]['operation'] = line[2].split(': new = old ')[-1]
    monkeys[name]['test'] = {}
    monkeys[name]['test']['divisible by'] = int(line[3].split("Test: divisible by ")[-1])
    monkeys[name]['test']['true'] = line[4].split(": throw to ")[-1]
    monkeys[name]['test']['false'] = line[5].split(": throw to ")[-1]
    monkeys[name]['inspected items'] = 0

for round in range(20):
    for monkey, details in monkeys.items():
        operation = monkeys[monkey]['operation'].split()
        for item in monkeys[monkey]['items']:
            worry_level = item
            if operation[0] == '*':
                if operation[1] == 'old':
                    worry_level *= worry_level
                else:
                    worry_level *= int(operation[1])
            elif operation[0] == '+':
                if operation[1] == 'old':
                    worry_level += worry_level
                else:
                    worry_level += int(operation[1])
            # worry_level = math.floor(worry_level / 3)
            if worry_level % monkeys[monkey]['test']['divisible by'] == 0:
                name = monkeys[monkey]['test']['true']
                monkeys[name]['items'].append(worry_level)
            else:
                name = monkeys[monkey]['test']['false']
                monkeys[name]['items'].append(worry_level)
            monkeys[monkey]['inspected items'] += 1
            monkeys[monkey]['items'] = []

inspected_items = []
for name, value in monkeys.items():
    inspected_items.append(monkeys[name]['inspected items'])
inspected_items.sort()
print(inspected_items)
print(inspected_items[-1] * inspected_items[-2])