# #1. Length in cm - integer in the interval [10… 500]
# 2. Width in cm - an integer in the interval [10… 300]
# 3. Height in cm - an integer in the interval [10… 200]
# 4. Percentage - real number in the interval [0.000… 100.000]

length = int(input())
width = int(input())
height = int(input())
percentage = float(input())
volume = length * width * height

volume_in_lt = volume/1000
needed_liters = volume_in_lt * (1 - (percentage/100))

print(needed_liters)