your_dict = {'A': 1, 'B': 2, 'C':3}  #A for Rock, B for Paper, and C for Scissors
my_dict = {'X': 1, 'Y': 2, 'Z':3}  #X for Rock, Y for Paper, and Z for Scissors

total_points = 0
with open('day_two_input_data.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        you, me = line.split(' ')
        won_points = 0

        if me == "X":
            if you == 'A':
                me = "Z"
            elif you == "B":
                me = 'X'
            elif you == "C":
                me = 'Y'
        elif me == "Y":
            if you == 'A':
                me = "X"
            elif you == "B":
                me = "Y"
            elif you == "C":
                me = "Z"
        elif me == "Z":
            if you == 'A':
                me = "Y"
            elif you == "B":
                me = "Z"
            elif you == "C":
                me = "X"

        if me == "X":
            if you == 'A':
                won_points = 3
            if you == "C":
                won_points = 6
        elif me == "Y":
            if you == "A":
                won_points = 6
            if you == 'B':
                won_points = 3
        elif me == "Z":
            if you == 'B':
                won_points = 6
            if you == 'C':
                won_points = 3
        total_points += my_dict[me] + won_points
print(total_points)

