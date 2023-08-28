packets_pens = int(input())
packets_markers = int(input())
board_cleaner_liters = int(input())
discount = int(input())

price_packets_pens = 5.80 * packets_pens
price_packets_markers = 7.20 * packets_markers
price_board_cleaner = 1.20 * board_cleaner_liters

sum_without_discount = price_packets_pens + price_packets_markers + price_board_cleaner
discount = sum_without_discount * (discount/100)
sum = sum_without_discount - discount

print(sum)