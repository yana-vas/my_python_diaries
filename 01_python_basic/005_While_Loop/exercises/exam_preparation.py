maximum_failed_assessment = int(input())
exercise_name = input()

failed_times = 0
solved_problems = 0
assessment_sum = 0
last_exercises_name = " "

while exercise_name != "Enough":
    assessment = int(input())

    if assessment <= 4:
        failed_times += 1
        if failed_times > maximum_failed_assessment or failed_times == maximum_failed_assessment:
            break
    assessment_sum += assessment
    solved_problems += 1
    last_exercises_name = exercise_name
    exercise_name = input()
if exercise_name == "Enough":
    # Average score: 5.25
    # Number of problems: 4
    # Last problem: Bus
    print(f"Average score: {(assessment_sum / solved_problems):.2f}")
    print(f"Number of problems: {solved_problems}")
    print(f"Last problem: {last_exercises_name}")
else:
    print(f"You need a break, {failed_times} poor grades.")


