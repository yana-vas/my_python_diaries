city = input()
sales_volume = float(input())

if sales_volume < 0:
    print("error")
else:
    if city == "Sofia":
        commission = 0
        if 0 <= sales_volume <= 500:
            commission = sales_volume * 0.05
        elif 500 < sales_volume <= 1000:
            commission = sales_volume * 0.07
        elif 1000 < sales_volume <= 10000:
            commission = sales_volume * 0.08
        elif sales_volume > 10000:
            commission = sales_volume * 0.12
        print(f"{commission:.2f}")
    elif city == "Varna":
        commission = 0
        if 0 <= sales_volume <= 500:
            commission = sales_volume * 0.045
        elif 500 < sales_volume <= 1000:
            commission = sales_volume * 0.075
        elif 1000 < sales_volume <= 10000:
            commission = sales_volume * 0.1
        elif sales_volume > 10000:
            commission = sales_volume * 0.13
        print(f"{commission:.2f}")
    elif city == "Plovdiv":
        commission = 0
        if 0 <= sales_volume <= 500:
            commission = sales_volume * 0.055
        elif 500 < sales_volume <= 1000:
            commission = sales_volume * 0.08
        elif 1000 < sales_volume <= 10000:
            commission = sales_volume * 0.12
        elif sales_volume > 10000:
            commission = sales_volume * 0.145
        print(f"{commission:.2f}")
    else:
        print("error")



