actors_name = input()
point_form_the_academy = float(input())
evaluators = int(input())

total_points = point_form_the_academy
for i in range(evaluators):
    evaluator_name = input()
    points = float(input())
    length_name = len(evaluator_name)
    total_points += ((length_name * points)/2)
    if total_points > 1250.5:
        break
if total_points > 1250.5:
    print(f"Congratulations, {actors_name} got a nominee for leading role with {total_points:.1f}!")
else:
    needed_points = abs(1250.5 - total_points)
    print(f"Sorry, {actors_name} you need {needed_points:.1f} more!")