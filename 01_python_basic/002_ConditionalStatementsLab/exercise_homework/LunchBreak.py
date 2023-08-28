import math

series_name = input()
episode_duration = int(input())
break_duration = int(input())

time_for_lunch = break_duration/8
time_for_rest = break_duration/4

time_left = break_duration - time_for_lunch - time_for_rest

if time_left >= episode_duration:
    free_minutes = math.ceil(time_left - episode_duration)
    print(f"You have enough time to watch {series_name} and left with {free_minutes} minutes free time.")
else:
    needed_time = math.ceil(abs(episode_duration - time_left))
    print(f"You don't have enough time to watch {series_name}, you need {needed_time} more minutes.")