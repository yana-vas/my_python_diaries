number_of_snowballs = int(input())

highest_value = 0

highest_snowball_weight = 0
highest_time_needed = 0
highest_snowball_quality = 0
for i in range(number_of_snowballs):
    current_snowball_weight = int(input())
    current_time_needed = int(input())
    current_snowball_quality = int(input())
    current_value = (current_snowball_weight / current_time_needed) ** current_snowball_quality
    if current_value > highest_value:
        highest_value = current_value
        highest_snowball_weight = current_snowball_weight
        highest_time_needed = current_time_needed
        highest_snowball_quality = current_snowball_quality
print(f"{highest_snowball_weight} : {highest_time_needed} = {int(highest_value)} ({highest_snowball_quality})")

