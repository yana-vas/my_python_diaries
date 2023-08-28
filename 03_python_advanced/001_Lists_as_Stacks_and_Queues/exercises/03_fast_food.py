from collections import deque

food_quantity = int(input())
orders = deque(list(map(int, input().split(' '))))
biggest_order = max(orders)
for i in range(len(orders)):
    order = orders[0]
    if order <= food_quantity:
        food_quantity -= order
        orders.popleft()
    else:
        break
print(biggest_order)
orders = list(map(str, orders))
if len(orders) > 0:
    print(f"Orders left: {' '.join(orders)}")
else:
    print("Orders complete")