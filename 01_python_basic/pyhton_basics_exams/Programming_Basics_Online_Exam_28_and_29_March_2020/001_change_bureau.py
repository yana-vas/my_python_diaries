bitcoin = int(input())
chinese_yuan = float(input())
commission = float(input())
price_in_bgn = bitcoin * 1168 + chinese_yuan * 0.15 * 1.76
commission_price = commission * price_in_bgn / 1.95 * 0.01
price = price_in_bgn / 1.95 - commission_price

print(f"{price:.2f}")