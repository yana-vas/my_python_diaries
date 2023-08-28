import math

record_in_seconds = float(input())
distance_in_meters = float(input())
time_for_one_meter_in_seconds = float(input())

slows_down_every_15_minutes = math.floor(distance_in_meters / 15)
resistance = slows_down_every_15_minutes * 12.5

time_without_the_resistance = distance_in_meters * time_for_one_meter_in_seconds
time = time_without_the_resistance + resistance

if time < record_in_seconds:
    print(f" Yes, he succeeded! The new world record is {time:.2f} seconds.")
else:
    needed_time = time - record_in_seconds
    print(f"No, he failed! He was {needed_time:.2f} seconds slower.")



