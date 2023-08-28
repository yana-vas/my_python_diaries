people_in_the_jury = int(input())
command = input()
all_average_grade = 0
grades_counter = 0
while command != "Finish":
    average_grade = 0
    for i in range(people_in_the_jury):
        assessment = float(input())
        average_grade += assessment
        all_average_grade += assessment
        grades_counter += 1
    print(f"{command} - {average_grade/people_in_the_jury:.2f}.")
    command = input()
print(f"Student's final assessment is {all_average_grade/grades_counter:.2f}.")

