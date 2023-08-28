actors_name = input()
points_academy = float(input())
evaluators = int(input())
points = points_academy
for i in range(evaluators):
    evaluator_name = input()
    points_from_the_evaluator = float(input())
    points += len(evaluator_name) * points_from_the_evaluator / 2

    if points > 1250.5:
        break
if points > 1250.5:
    print(f"Congratulations, {actors_name} got a nominee for leading role with {points:.1f}!")
else:
    print(f"Sorry, {actors_name} you need {(1250.5 - points):.1f} more!")
