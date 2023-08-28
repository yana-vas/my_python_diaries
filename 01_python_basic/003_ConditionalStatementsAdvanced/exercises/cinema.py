projection = input()
rows = int(input())
columns = int(input())

seats = rows * columns
price = 0
if projection == "Premiere":
    price = seats * 12.00
elif projection == "Normal":
    price = seats * 7.50
elif projection == "Discount":
    price = seats * 5.00
print(f"{price:.2f} leva")
