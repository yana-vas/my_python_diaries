n = int(input())
reservations = set()
coming = set()
for _ in range(n):
    reservation_code = input()
    reservations.add(reservation_code)

command = input()
while command != 'END':
    coming.add(command)
    command = input()

not_coming = list(reservations.difference(coming))
print(len(not_coming))

vip = []
regular = []
for code in not_coming:
    if code[0].isdigit():
        vip.append(code)
    else:
        regular.append(code)
vip = sorted(vip)
regular = sorted(regular)
for v_code in vip:
    print(v_code)
for r_code in regular:
    print(r_code)
