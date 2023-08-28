shooting_time = int(input())
scenes = int(input())
scenes_duration = int(input())
prep_time = 15*shooting_time*0.01
if (prep_time + (scenes * scenes_duration)) <= shooting_time:
    left_time = shooting_time - (prep_time + (scenes * scenes_duration))
    print(f"You managed to finish the movie on time! You have {round(left_time)} minutes left!")
else:
    needed_time = (prep_time + (scenes * scenes_duration)) - shooting_time
    print(f"Time is up! To complete the movie you need {round(needed_time)} minutes.")