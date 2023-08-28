command = input()

sum_time = 0
one_lesson = 45

while command != "stop":
    command = int(command)
    minutes = int(input())

    hours_in_minutes = command * 60
    sum_time += hours_in_minutes + minutes

    command = input()
all_lessons = sum_time // 45
plus_minutes = sum_time % 45

print(f"The lessons are {all_lessons}")
print(f"there are {plus_minutes} minutes plus")
