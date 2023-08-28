budget = float(input())
number_video_cards = int(input())
number_processors = int(input())
number_memory_frames = int(input())
price_for_video_cards = number_video_cards * 250

price = price_for_video_cards + (number_processors * (price_for_video_cards * 0.35)) + (number_memory_frames * (price_for_video_cards * 0.1))

if number_video_cards > number_processors:
    price -= (price * 0.15)
if price <= budget:
    left_money = budget - price
    print(f"You have {left_money:.2f} leva left!")
else:
    needed_money = abs(price - budget)
    print(f"Not enough money! You need {needed_money:.2f} leva more!")