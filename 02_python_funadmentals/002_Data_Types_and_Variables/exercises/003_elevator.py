number_of_people = int(input())
capacity = int(input())
needed_courses = 0
if number_of_people < capacity:
    needed_courses = 1
else:
    needed_courses = number_of_people//capacity
    if not number_of_people % capacity == 0:
        if number_of_people % capacity < (number_of_people-needed_courses):
            needed_courses += 1
        else:
            needed_courses += number_of_people % capacity

print(needed_courses)
