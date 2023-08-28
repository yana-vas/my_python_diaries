# destination = input()
# current_sum = 0
# while destination != "End":
#     budget = float(input())
#     current_money = 0
#     while current_money < budget:
#         current_money = float(input())
#         current_sum += current_money
#         if current_sum >= budget:
#             print(f"Going to {destination}!")
#             continue
destination = input()

while destination != "End":
    price_trip = float(input())
    current_sum = 0
    while current_sum < price_trip:
        money = float(input())
        current_sum += money
    print(f"Going to {destination}!")

    destination = input()

