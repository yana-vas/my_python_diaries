actors_name = input()
point_from_the_academy = float(input())
number_of_evaluators = int(input())
points = 0
for i in range(number_of_evaluators):
    name_of_the_evaluator = input()
    points_from_the_evaluator = float(input())
    evaluator_name_length = len(name_of_the_evaluator) * points_from_the_evaluator * 2
    points += points_from_the_evaluator
    if points > 1250.5:
        break


if points > 1250.5:
    print(f"Congratulations, {actors_name} got a nominee for leading role with {points - 1250.5:.1f}!")
else:
    points_needed = 1250.5 - points
    print(f"Sorry, {actors_name} you need {points_needed:.1f} more!")






