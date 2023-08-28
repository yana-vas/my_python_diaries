command = input()
courses = {}
while command != 'end':
    command = command.split(" : ")
    course_name = command[0]
    student_name = command[1]
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)
    command = input()

for course, names in courses.items():
    print(f"{course}: {len(names)}")
    for name in names:
        print(f"-- {name}")
