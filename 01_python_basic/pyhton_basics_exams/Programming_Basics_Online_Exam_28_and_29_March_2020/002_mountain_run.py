record_in_sc = float(input())
distance_in_mt = float(input())
the_time_needed_for_one_mt = float(input())
delay = distance_in_mt // 50 * 30
time = the_time_needed_for_one_mt * distance_in_mt + delay
if time < record_in_sc:
    print(f" Yes! The new record is {time:.2f} seconds.")
else:
    needed_seconds = time - record_in_sc
    print(f"No! He was {needed_seconds:.2f} seconds slower.")