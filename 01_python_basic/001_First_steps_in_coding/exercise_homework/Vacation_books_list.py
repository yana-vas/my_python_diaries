number_of_pages = int(input())
pages_for_hour = int(input())
days = int(input())

hours_needed = number_of_pages // pages_for_hour
needed_hours_for_day = hours_needed // days
print(needed_hours_for_day)