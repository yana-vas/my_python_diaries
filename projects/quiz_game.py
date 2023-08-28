import random

import math

print("Welcome to my computer game")

playing = input('Do you want to play? ')
questions = {"What does CPU stand for?": {'hint': 'PU stand for processing unit', 'answer': "central processing unit"},
             "What does GPU stand for?": {'hint': 'PU stand for processing unit', 'answer': "graphics processing unit"},
             "What does RAM stand for?": {'hint': 'RA stand for random access', 'answer': "random access memory"},
             "What does PSU stand for?": {'hint': 'SU stand for supply', 'answer': "power supply"},
             "What is parameter": {'hint': 'it is used in function', 'answer': 'variable defined in function definition'},
             "What is argument": {'hint': 'it is used outside the function body', 'answer': 'actual value passed to the function'},
             "What is append()": {'hint': 'it is used in lists', 'answer': 'add single element at the end'},
             "What is extend()": {'hint': 'it is used in lists', 'answer': 'add multiple elements at the end'},
             "What is insert()": {'hint': 'it is used in lists', 'answer': 'Add single element at a specific index'}}
if playing.lower() != 'yes':
    quit()
print("Okay! Let's play :)")
score = 0
hints = 3
incorrect_answers = 0
for i in range(len(questions)):
    question = random.choice(list(questions.keys()))
    print(f"Next question: {question}")
    answer = input().lower()
    if answer == questions[question]['answer']:
        print("Correct!")
        score += 1
    elif answer == 'hint':
        if hints > 0:
            hints -= 1
            print(questions[question]['hint'])
        else:
            print('No more hints :(')
        answer = input().lower()
        if answer == questions[question]['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    else:
        print("Incorrect!")
    del questions[question]
    if incorrect_answers > 3:
        break

print('-------------------------------')
print("End Game")
print(f"You got {score} questions correct!")
print(f"You got {math.floor((score / 4) * 100)}%.")
