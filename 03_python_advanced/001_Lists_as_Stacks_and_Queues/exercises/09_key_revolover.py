from collections import deque

bullet_price = int(input())
size_gun_barrel = int(input())
bullets = list(map(int, input().split(' ')))
locks = deque(list(map(int, input().split(' '))))
intelligence = int(input())

i = size_gun_barrel
wasted_bullets = 0
while bullets:
    if len(locks) == 0:
        break
    current_lock = locks[0]
    current_bullet = bullets.pop()
    if current_lock >= current_bullet:
        print('Bang!')
        locks.popleft()
    else:
        print('Ping!')
    i -= 1
    wasted_bullets += 1
    if i == 0 and len(bullets) > 0:
        print("Reloading!")
        i = size_gun_barrel

if len(locks) == 0:
    print(f"{len(bullets)} bullets left. Earned ${intelligence-(wasted_bullets * bullet_price)}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")