import math

serial_name = input()
seasons = int(input())
episodes = int(input())
episode_duration_without_ads = float(input())
episode_duration_with_ads = episode_duration_without_ads + (20*episode_duration_without_ads/100)
bonus_time = seasons * 10
all_time_for_watching = episode_duration_with_ads * episodes * seasons + bonus_time

print(f"Total time needed to watch the {serial_name} series is {math.floor(all_time_for_watching)} minutes.")
