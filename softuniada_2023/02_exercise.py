n = int(input())

width = n+5
rocket = []
half_width = ((n+5)//2)
first_row = half_width*'_'+ '^' + half_width*'_'
rocket.append(first_row)

half_width -= 1
second_row = half_width*'_' + "/|\\" + half_width*'_'
rocket.append(second_row)
for i in range(half_width):
    second_half = i*'.' + '\\' + (half_width-(i+1))*'_'
    first_half = (half_width-(i+1))*'_' + '/' + i*'.'
    row = first_half + '|||' + second_half
    rocket.append(row)
rocket.append(rocket[-2])
for i in range(n):
    row = half_width*'_' + "|||" + half_width*'_'
    rocket.append(row)
new_row = half_width*'_' + "~~~" + half_width*'_'
rocket.append(new_row)
half_width -= 1

for i in range(half_width):
    second_half = i*'.' + 2*'\\' + (half_width-(i))*'_'
    first_half = (half_width - (i)) * '_' + '//' + i * '.'
    row = first_half + '!' + second_half
    rocket.append(row)

print('\n'.join(rocket))