names = input().split(", ")
sorted_list = sorted(names)
sorted_list = sorted(sorted_list, key=lambda name: -len(name))
print(sorted_list)