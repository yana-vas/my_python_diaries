rooms = int(input())
free_chairs = 0
is_not_enough_chairs = False
for current_room in range(1, rooms+1):
    chairs_and_people = input().split(' ')
    chairs = len(chairs_and_people[0])
    people = int(chairs_and_people[1])
    if chairs < people:
        is_not_enough_chairs = True
        print(f"{people-chairs} more chairs needed in room {current_room}")
    else:
        free_chairs += chairs - people
if not is_not_enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")